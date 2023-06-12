# ceshia = 1
# def x_add_a(panding):
        #     jisuan = 1
        #     def quzhi():
        #         nonlocal jisuan
        #         canvas.move(button_demo, -1, 0)
        #         jisuan += 1
        #         if jisuan < panding:
        #             canvas.after(3, quzhi())
        #         else:
        #             return
        #     quzhi()
        #     return jisuan

        # leiji = 1
        # print("c-", str(panding))
        # if panding < 80:
        #     canvas.move(button_demo, -1, 0)
        #     panding += 1
        #     leiji += 1
        #     print(panding)
        #     if panding < 80:
        #         canvas.after(3, lambda: x_add_a(panding))
        #     elif panding >= 80:
        #         print(1)
        #         nonlocal ceshia
        #         ceshia = panding
        #         return

        # def x_add_b():
        #     canvas.move(button_demo, 1, 0)
        #     canvas.after(3, x_add_b)
        #
        # def y_add():
        #     canvas.move(button_demo, 0, 1)
        #     canvas.after(3, y_add)
        #
        # if yanshi_fenli == 1:
        #     def button_move():
        #         nonlocal x, y
        #         if x < 80:
        #             dezhi = x_add_a(80)
        #             print("a" + str(dezhi))
        #             # print("a" + str(x))
        #         elif x >= 80:
        #             if y < 145:
        #                 canvas.move(button_demo, 0, 1)
        #                 c = canvas.after(3, button_move)
        #                 u.append(c)
        #                 y += 1
        #                 # print(y)
        #             elif y >= 145:
        #                 if x < 542:
        #                     canvas.move(button_demo, -1, 0)
        #                     a = canvas.after(3, button_move)
        #                     x += 1
        #                 #     print("b" + str(x))
        #                 # print(u)
        #         if x == 542:
        #             canvas.delete(button_demo)
        #             canvas.after_cancel(a)
        #             # canvas.after_cancel(b)
        #             # canvas.after_cancel(c)
        #             x = 0
        #             yanshi(1)
        #             return
        #
        #     button_move()
        # elif yanshi_fenli == 2:
        #     def button_move():
        #         nonlocal x
        #         if x < 267:
        #             canvas.move(button_demo, -1, 0)
        #             a = canvas.after(6, button_move)
        #             x += 1
        #             print("指引二" + str(x))
        #         if x >= 267:
        #             x = 0
        #             canvas.delete(button_demo)
        #             canvas.after_cancel(a)
        #             yanshi(2)
        #             return
        #
        #     button_move()
        # elif yanshi_fenli == 3:
        #     def button_move():
        #         nonlocal x, y
        #         if x < 80:
        #             canvas.move(button_demo, -1, 0)
        #             canvas.after(3, button_move)
        #             x += 1
        #             print(x)
        #         elif x >= 80:
        #             if y < 145.5:
        #                 canvas.move(button_demo, 0, 1)
        #                 canvas.after(3, button_move)
        #                 y += 1
        #                 print(y)
        #             elif y >= 145.5:
        #                 if x < 160:
        #                     canvas.move(button_demo, -1, 0)
        #                     canvas.after(3, button_move)
        #                     x += 1
        #                     print(x)
        #                 elif x >= 160:
        #                     canvas.move(button_demo, 0, 1)
        #                     d = canvas.after(3, button_move)
        #                     y += 1
        #                     print(y)
        #         if y == 193:
        #             canvas.delete(button_demo)
        #             canvas.after_cancel(d)
        #             yanshi(3)
        #             return
        #
        #     button_move()