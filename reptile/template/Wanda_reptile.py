import requests
from bs4 import BeautifulSoup

from template import CSVInput


class WandaReptile:

    def __init__(self):
        headers = {

            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"
        }

        tiaomu = 0
        tiaomu_guanjianci = 0

        with open("./DataSet/万达‘停车’方面评论.txt", "a", encoding="UTF-8") as f:
            csv_handler = CSVInput.CSVHandler("./DataSet/ScoreAnalysis_Dataset.csv",
                                              ["总体打分项", "总体打分", "分数最低名称", "分数最低数值", "分数最高数值",
                                               "总评分数"])
            guanjiandian_zongshu, guanjiandian_shangpin, guanjiandian_huanjing, guanjiandian_fuwu = 0, 0, 0, 0
            for index in range(1, 10, 1):
                global yema
                if index == 1:
                    yema = ""
                    print("-p1")
                elif index != 1 and index >= 0:
                    yema = f"-p{index}"
                print(yema)
                response = requests.get(f"https://you.ctrip.com/shopping/shanghai2/1370875-dianping{yema}.html",
                                        headers=headers)
                if response.status_code == 200 or response.ok:
                    HTML_Value = BeautifulSoup(response.text, "html.parser")
                    PinglunquDIV = HTML_Value.findAll("div", attrs={"class": "comment_ctrip"})

                    for i in PinglunquDIV:
                        PinglunText = i.findAll("span", attrs={"class": "heightbox"})
                        Guanjiandian = i.findAll("span", attrs={"class": "sblockline"})
                        for j in Guanjiandian:
                            fenbietiqu = list("".join([dt.strip(' ') for dt in j.text]))
                            fenbietiqutext = ("".join(
                                fenbietiqu[fenbietiqu.index("商"):fenbietiqu.index("商") + 5]) + "".join(
                                fenbietiqu[fenbietiqu.index("环"):fenbietiqu.index("环") + 5]) + "".join(
                                fenbietiqu[fenbietiqu.index("服"):fenbietiqu.index("服") + 5])).split("\u2003")
                            fenbietiqutext.pop(-1)
                            fenbietiqutuple = []
                            for tuples in fenbietiqutext:
                                fenbietiqutuple.append(tuple((tuples[0:2],) + (tuples[3:4],)))
                            fenbietiqudict = dict(fenbietiqutuple)
                            # print(fenbietiqutext, "____", len(fenbietiqutext))
                            guanjiandian_zongshu += 1
                            duibi = []
                            duibi_keys = []
                            for tiqu_values in fenbietiqudict.values():
                                duibi.append(tiqu_values)
                            for tiqu_keys in fenbietiqudict.keys():
                                duibi_keys.append(tiqu_keys)
                            minValue = min(duibi)
                            maxValue = max(duibi)
                            print("总体打分项：", fenbietiqudict)
                            print("总体打分：", duibi)
                            print("分数最低为：", f"名称为：{duibi_keys[duibi.index(minValue)]}", f"值为：{minValue}")
                            print("分数最高为：", maxValue)

                            if int(minValue) != int(maxValue):
                                csv_handler.append_row(
                                    [fenbietiqudict, duibi, duibi_keys[duibi.index(minValue)], minValue, maxValue, "-"])

                        print(len(PinglunText))

                        print("关键点总数：", guanjiandian_zongshu)
                        tiaomu += len(PinglunText)
                        guanjiance = ["车", "停车", "car", "stop"]
                        for j in PinglunText:
                            for n in guanjiance:
                                if n in j.text:
                                    print(j.text, "\n")
                                    tiaomu_guanjianci += 1
                                    f.write("\n" * 2 + f"message:{str(tiaomu_guanjianci)}" + "\n" + j.text + "\n")
                                    break

                else:
                    print("爬取数据执行有误，请在检查其数据内容有效性后重新进行爬取！")
        csv_handler.append_row(["", "", "", "", "", guanjiandian_zongshu])
        print(f"评论总条目:{tiaomu},", f"含有“车”、“停车”、“car”、“stop”关键词的评论条目数：{tiaomu_guanjianci}")
