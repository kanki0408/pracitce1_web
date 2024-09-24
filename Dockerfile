# ベースイメージとしてPython 3.12.6を指定
FROM python:3.12.6

# 作業ディレクトリの設定
WORKDIR /app

# 必要なツールのインストール
RUN apt-get update && apt-get install -y curl

# Poetryのインストール
RUN curl -sSL https://install.python-poetry.org | python3 -

# Poetryをパスに追加
ENV PATH="/root/.local/bin:$PATH"

# Poetryで仮想環境を作らないように設定
RUN poetry config virtualenvs.create false

# pyproject.tomlとpoetry.lockをコピー
COPY pyproject.toml poetry.lock* ./

# 依存関係のインストール
RUN poetry install --no-root

# アプリケーションコードをコピー
COPY . .

# Flaskの環境変数を設定してアプリケーションを起動
CMD ["flask", "run", "--host=0.0.0.0"]
