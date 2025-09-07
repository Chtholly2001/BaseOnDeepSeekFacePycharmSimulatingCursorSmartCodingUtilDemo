
import os
import time
import random
import string
import pyautogui
import subprocess
import requests

# ==== 路径配置 ====
project_path = r"C:\Users\chtho\PycharmProjects\Yursor\TargetFilesDirectory"

# ==== PyCharm 路径 ====
pycharm_exe = r"C:\Program Files\JetBrains\PyCharm 2025.1.1.1\bin\pycharm64.exe"

# ==== DeepSeek API 配置 ====
API_KEY = "你的deepseek key"
API_URL = "https://api.deepseek.com/v1/chat/completions"

# ==== 生成随机文件名 ====
def random_filename(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) + ".py"

# ==== AI 生成代码 ====
def ai_generate_code(error_msg=None):
    if not error_msg:
        user_prompt = input("1.请输入你要生成的Python功能需求，注意，提示词决定成败，可以先把需求喂给ChatGPT，再把提示词提交到这里，\n\n2.例如，合格的提示词应该是这样的，请写一个清晰、可运行的联网 Python 脚本提示词，提示词应满足以下特征：\n说明脚本要完成的具体任务（如获取电影名、IP地址、新闻标题等），\n明确要访问的数据来源（如豆瓣、ipify、百度新闻等知名站点或开放API），\n使用常见的 Python 网络库（如 requests）完成请求，\n明确指定输出结果的方式（如“打印在控制台”、“输出到文件”），\n任务结构应简单，能在一次代码生成中完成“请求→解析→输出”的闭环，\n\n3.鼠标在主程序与生成程序之间切换以完成聚焦：\n>> ")
    else:
        user_prompt = f"之前代码错误：{error_msg}\n请生成修复后的代码。"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    json_data = {
        "model": "deepseek-chat",
        "temperature": 0.2,
        "max_tokens": 10000,
        "messages": [
            {"role": "system", "content": (
                "你是一个专业的Python代码生成器。请根据用户的功能需求，生成完整的、可直接运行的Python代码。请严格遵守以下要求： "
                "请根据用户需求，生成完整且可运行的Python代码脚本。"
                "代码需满足以下要求：\n"
                "1. 只输出纯Python代码，不要带任何Markdown代码块符号（比如 ```python、``` 等）。\n"
                "2. 不要添加任何额外的注释、解释或文字说明。\n"
                "3. 代码必须完整，包含必要的函数和入口。\n"
                "4. 代码风格规范，语法正确，能直接运行。\n"
                "5. 如果需求不明确，请基于合理推测生成示例代码。\n"
                "6. 仅在一个.py文件里就完成需求所需的所有完整代码。\n"
                "7. 尽可能不使用依赖。\n"
            )},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 1000
    }

    print("[→] 正在向 DeepSeek 请求生成代码...")
    try:
        response = requests.post(API_URL, headers=headers, json=json_data)
        response.raise_for_status()
        data = response.json()
        code = data['choices'][0]['message']['content']
        print("[✓] DeepSeek 返回代码成功")
        return code
    except Exception as e:
        print(f"[×] DeepSeek 请求失败：{e}")
        return 'print("DeepSeek 请求失败，请检查 API 密钥或网络。")'

# ==== 写入代码 ====
def write_code(code, filename):
    file_path = os.path.join(project_path, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"[✓] 写入代码：{file_path}")
    return file_path

# ==== 运行代码 ====
def run_code(file_path):
    result = subprocess.run(["python", file_path], capture_output=True, text=True, encoding="utf-8")
    return result.stdout, result.stderr

# ==== 打开 PyCharm 并运行 ====
def open_pycharm_and_run(file_path):
    print("[→] 启动 PyCharm 并加载代码文件...")
    os.system(f'start "" "{pycharm_exe}" "{file_path}"')
    time.sleep(10)  # 等 PyCharm 打开

    print("[→] 点击代码区域以确保焦点正确")
    pyautogui.click(x=800, y=500)  # 请根据你屏幕调整坐标
    time.sleep(1)

    print("[→] 模拟 Ctrl+Shift+F10 触发运行")
    pyautogui.hotkey('ctrl', 'shift', 'f10')
    print("[✓] PyCharm 已触发运行（请查看控制台）")

# ==== 主流程 ====
def main(max_attempts=3):
    filename = random_filename()
    code = ai_generate_code()
    for attempt in range(max_attempts):
        print(f"\n[尝试第 {attempt+1} 次]")
        file_path = write_code(code, filename)
        out, err = run_code(file_path)
        print("输出：", out)
        if err:
            print("错误：", err)
            code = ai_generate_code(err)
            time.sleep(1)
        else:
            print("[✓] 代码运行成功（命令行）！准备打开 PyCharm 自动执行")
            open_pycharm_and_run(file_path)
            break
    else:
        print("[×] 超过最大尝试次数，仍有错误，请手动检查代码。")

if __name__ == "__main__":
    main()
