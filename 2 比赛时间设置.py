# coding=utf-8
import toml

config_path = "D:\\awdManager\\conf\\Cardinal.toml"

config = toml.load(config_path)
print("时间样例: 2022-03-03T08:00:00")
config['base']['BeginTime'] = input("请输入开始时间: ") + "+08:00"
config['base']['EndTime'] = input("请输入结束时间: ") + "+08:00"
with open(config_path, 'w') as file:
    toml.dump(config, file)
