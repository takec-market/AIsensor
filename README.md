# AIsensor
[高齢者]
  │
  ├─▶ [ウェアラブル端末（加速度/ジャイロ）]
  │       └─▶ データ送信（Bluetooth/Wi-Fi）
  │
  ├─▶ [部屋のカメラ（RGB or 深度）]
  │       └─▶ 画像ストリーム or 動画解析
  │
  ▼
[中央処理ユニット（Raspberry Pi, PC, or クラウド）]
  ├─▶ センサーデータ解析（AIモデル）
  ├─▶ カメラ映像処理（姿勢推定や転倒検知）
  └─▶ 統合判断（センサ + 映像で判断精度UP）
      └─▶ アラート送信（家族/介護者に通知）
🎯 進め方（段階的）

第1段階：ウェアラブル型の構築
	•	【センサー選定】MPU6050 や 9軸IMU（加速度 + ジャイロ + 磁気）
	•	【プログラミング】Arduino or ESP32（BLE通信可能）
	•	【転倒判定ロジック】
	•	阈値判定（加速度が一定以上 & 姿勢が横向きで持続）
	•	or 簡易的なMLモデル（決定木やSVM）
	•	【通知】スマホやPCに送る仕組み（BLE, MQTT, HTTP, LINE APIなど）

第2段階：カメラ映像による転倒検知
	•	【カメラ】USBカメラ / Raspberry Pi Camera / Depth Camera (Intel RealSense等)
	•	【AI】以下のような姿勢推定ライブラリで「倒れている」状態を検出
	•	OpenPose / MediaPipe / YOLO-Pose
	•	【処理】フレームごとに姿勢を追跡 → 異常状態（急激な崩れ＋静止）で検知

第3段階：センサーデータと映像の統合
	•	ロジック例：
	•	両方異常 → 転倒確定
	•	片方のみ異常 → 一時的な誤動作 or 未確定 → 要継続観察 or 軽通知

分類
技術 or ツール
ウェアラブル開発
Arduino / ESP32 / M5Stack
通信
BLE / MQTT / HTTP
AI解析
Python + scikit-learn / TensorFlow Lite
映像処理
OpenCV + MediaPipe / YOLO
通知
LINE Messaging API / IFTTT / Twilio
本体
Raspberry Pi 4 / Jetson Nano（GPU必要なら）

## Docker環境

このリポジトリでは Python ベースの解析環境を Docker で提供しています。
以下のコマンドでイメージをビルドできます。

```bash
docker build -t aisensor .
```

### 実行例

```bash
docker run --rm aisensor
```

カメラデバイスやシリアルポートを利用する場合は `--device` オプションを追加してください。

## 導入方法

### Python 環境での実行

Python 3.9 以上がインストールされた環境で以下の手順を実行します。

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Docker を用いた実行

前述の通り、Docker イメージをビルドして起動することもできます。

```bash
docker build -t aisensor .
docker run --rm aisensor
```

必要に応じて `--device` オプションでカメラやシリアルポートをマウントしてください。

## テスト

テストには `pytest` を使用します。未インストールの場合は以下で追加してください。

```bash
pip install pytest
```

テストは `tests/` ディレクトリにあります。次のコマンドで実行できます。

```bash
pytest
```
