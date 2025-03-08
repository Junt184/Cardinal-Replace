import yaml
import re



def generate_docker_compose(num_targets, image_name, ports):
    def quoted_port_representer(dumper, data):
        """自定义YAML字符串表示器，为端口格式添加双引号"""
        if re.match(r'^\d+:\d+$', data):
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')
        return dumper.represent_str(data)

    # 注册自定义表示器
    yaml.add_representer(str, quoted_port_representer)
    """生成Docker Compose数据结构"""
    return {
        'version': '3.8',
        'services': {
            f"target{i+1}": {
                'image': image_name,
                'ports': [
                    f"{j* 100 + i}:{j}"     # SSH端口
                for j in ports ]
            } for i in range(num_targets)
        }
    }

if __name__ == '__main__':
    # 用户输入
    num_targets = 13
    image_name = "awd-server-1:latest"
    open_port = [22, 80, 3306]
    # 生成数据并写入文件
    with open('docker-compose.yml', 'w') as f:
        yaml.dump(
            generate_docker_compose(num_targets, image_name, open_port),
            f,
            default_flow_style=False,  # 禁用流式格式
            sort_keys=False,           # 保持键的顺序
            indent=2,                  # 设置缩进
            width=1000                 # 避免自动换行
        )

    print("docker-compose.yml 文件已生成！")