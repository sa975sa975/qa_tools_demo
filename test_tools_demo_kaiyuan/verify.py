# 输入框内容转化(测试环境)
def get_entry_env(entry_str):
    # 判断输入的字符
    for i in entry_str:
        if i == "-" or i.isalpha() or i.isdigit():
            continue
        else:
            return ""
    entry_num = ""
    if len(entry_str.split("-")) > 2:
        return ""
    else:
        pass
    # 生成测试环境
    if "-" not in entry_str:
        if "master" not in entry_str:
            return ""
        else:
            return'st-master.kingsgroupgames.com'
    elif "master" in entry_str:
        entry_num = entry_str.split("-")[1]
        if entry_num in ["new"]:
            return f'st-master-{entry_num}.kingsgroupgames.com'
        else:
            return ""
    elif "dev" in entry_str:
        entry_num = entry_str.split("-")[1]
        if entry_num == "":
            return ""
        elif entry_num.isdigit():
            return f'st-api-dev-{entry_num}.kingsgroup.cc'
        else:
            return ""
    elif "release" in entry_str:
        entry_num = entry_str.split("-")[1]
        if entry_num == "":
            return ""
        elif entry_num.isdigit():
            return f'st-api-release-{entry_num}.kingsgroup.cc'
        else:
            return ""
    else:
        return ""
    
# 输入框内容转化(测试uid列表)
def get_entry_uid_list(entry_str):
    # 判断输入的字符
    # print("1111111111")
    entry_str = entry_str.replace(" ", "")
    for index, i in enumerate(entry_str):
        if i == "-" or i == "," or i.isdigit() and (int(i) != 0 or index != 0) or i == " ":
            continue
        else:
            return []
    # print("222222222")
    if "-" in entry_str and "," in entry_str:
        return []
    # 1.顺序范围
    elif "-" in entry_str:
        min_uid_str, max_uid_str = "", ""
        if len(entry_str.split("-")) > 2:
            return []
        min_uid_str, max_uid_str = entry_str.split("-")
        if min_uid_str.isdigit() and max_uid_str.isdigit():
            if min_uid_str > max_uid_str:
                return []
            else:
                return list(range(int(min_uid_str), int(max_uid_str)+1))
        else:
            return []
    # 2.人为指定
    elif "," in entry_str:
        uid_list = [int(uid_str.strip()) for uid_str in entry_str.split(",") if uid_str != ""]
        uid_list = list(set(uid_list))
        return uid_list
    elif entry_str.isdigit():
        uid_list = [int(entry_str.strip())]
        uid_list = list(set(uid_list))
        return uid_list
    else:
        return []
    

# 判断双参数中参数a
def get_entry_parama_1(entry_str):
    # 条件语句
    return entry_str

# 判断双参数中参数b
def get_entry_parama_2(entry_str):
    # 条件语句
    return entry_str