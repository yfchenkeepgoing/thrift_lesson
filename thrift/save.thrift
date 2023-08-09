namespace cpp save_service

service Save {

     # username: myserver的名称，我的username是acs_11385
     # password: myserver的密码的md5值的前8位，用命令md5sum，我的password是bbc7baa1
     # 由加密后的信息反推原密码很难，因此不用担心密码泄露的问题
     # 用户名密码验证成功会返回0，验证失败会返回1
     # 验证成功后，结果会被保存到myserver:homework/lesson_6/result.txt中
     i32 save_data(1: string username, 2: string password, 3: i32 player1_id, 4: i32 player2_id)
     # 前两个参数用于验证身份，后两位参数是匹配的两个玩家的id
}

