import matplotlib.pyplot as plt
from random import uniform

# 用于保存所有的位置点
points = []

# 这是一个用于模拟位置改变的函数
def get_location():
    if len(points) == 0:
        # 初始位置
        lat, lon = uniform(-90, 90), uniform(-180, 180)
    else:
        # 基于前一个点的位置生成新点
        prev_lat, prev_lon = points[-1]
        lat = prev_lat + uniform(-1, 1)
        lon = prev_lon + uniform(-1, 1)

        # 限制纬度的范围在 -90 到 90 之间
        lat = max(min(lat, 90), -90)

        # 限制经度的范围在 -180 到 180 之间
        if lon > 180:
            lon -= 360
        elif lon < -180:
            lon += 360

    return lat, lon

# 创建一个地图
fig, ax = plt.subplots()

# 设置x, y轴的限制
ax.set_xlim([-180, 180])
ax.set_ylim([-90, 90])

# 每秒更新位置
while len(points) < 20000:
    lat, lon = get_location()

    # 保存新的位置点
    points.append((lat, lon))

# 清除之前的点和线
ax.clear()

# 重新设置x, y轴的限制
ax.set_xlim([-180, 180])
ax.set_ylim([-90, 90])

# 绘制所有的位置点
lats, lons = zip(*points)
ax.plot(lons, lats, marker='o')

# 绘制矢量连接
# for i in range(len(points) - 1):
#     lat1, lon1 = points[i]
#     lat2, lon2 = points[i + 1]
#     ax.plot([lon1, lon2], [lat1, lat2], 'b-')

# 显示图像
plt.show()
