from flask import Flask

app = Flask(__name__)  # __name__ 代表目前執行的模組

# @app.route 用來定義路由, 表達式: @app.route(你的url) 而('/') 為 根目錄
@app.route('/') # 函式的裝飾 (Decorator): 以函式為基礎, 提供附加的功能 
def home():
    return "I Love Even"

@app.route('/test') # 代表我們要處理的網站路徑
def test():
    return "This is Test"


if __name__ == "__main__":  # 如果以主程式(__main__)執行
    app.debug = True
    app.run()  # 立刻啟動伺服器
