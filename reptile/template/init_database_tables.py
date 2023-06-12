import mysql.connector
from mysql.connector import errorcode


def initialize_database():
    try:
        # 连接到MySQL服务器
        cnx = mysql.connector.connect(
            user='root',
            password='744214Sgg',
            host='localhost'
        )
        #
        # 创建游标对象
        cursor = cnx.cursor()

        # 创建数据库
        create_database_query = "CREATE DATABASE IF NOT EXISTS `reptile_values` DEFAULT CHARACTER SET utf8;"

        cursor.execute(create_database_query)

        # 选择数据库
        cursor.execute("USE `reptile_values`")

        # 创建数据表
        create_table_query1 = """
        CREATE TABLE `button_states` (
          `button_id` int NOT NULL AUTO_INCREMENT,
          `color` varchar(45) DEFAULT NULL,
          `text` varchar(45) DEFAULT NULL,
          `LicensePlateNumber` varchar(145) DEFAULT NULL,
          `DateOfNntry` datetime DEFAULT NULL,
          PRIMARY KEY (`button_id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;
        """
        cursor.execute(create_table_query1)

        # 提交更改并关闭连接
        cnx.commit()

        create_table_query2 = """
                    CREATE TABLE `users` (
                        `username` varchar(255) DEFAULT NULL
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
                """
        cursor.execute(create_table_query2)

        # 提交更改并关闭连接
        cnx.commit()

        insert_table_query = """
        INSERT INTO `reptile_values`.`button_states`
            (
            `button_id`,
            `color`,
            `text`
            )
        VALUES
            (%s, %s, %s);
        """

        datas = [
            ('1','#DC8439', '1号停车位（可用）'),
            ('2', '#DC8439', '2号停车位（可用）'),
            ('3', '#DC8439', '3号停车位（可用）'),
            ('4', '#DC8439', '4号停车位（可用）'),
            ('5', '#DC8439', '5号停车位（可用）'),
            ('6', '#DC8439', '6号停车位（可用）'),
            ('7', '#DC8439', '7号停车位（可用）'),
            ('8', '#DC8439', '8号停车位（可用）'),
            ('9', '#DC8439', '9号停车位（可用）'),
            ('10', '#DC8439', '10号停车位（可用）'),
            ('11', '#DC8439', '11号停车位（可用）'),
            ('12', '#DC8439', '12号停车位（可用）'),
            ('13', '#DC8439', '13号停车位（可用）'),
            ('14', '#DC8439', '14号停车位（可用）')
        ]

        for data in datas:
            cursor.execute(insert_table_query, data)
            cnx.commit()

        cursor.close()
        cnx.close()

        print("数据库初始化完成！")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("数据库访问被拒绝，请检查用户名和密码。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("数据库不存在，请确保数据库名称正确。")
        else:
            print("发生错误：", err)
