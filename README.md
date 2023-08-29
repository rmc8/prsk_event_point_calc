# prsk_event_point_calc

**\* English follows Japanese**

このRepositoryでは、イベントポイントの計算結果を公開しています。

## データの形式とアクセス方法
- **tableディレクトリ** : TSV形式で計算結果を参照できます。
- **apiディレクトリ** : JSON形式で計算結果を配信しています。

## データの作成方法
- `calc.py` : tableディレクトリ内のデータを作成します。
- `create_json.py` : tableディレクトリのデータからapiディレクトリのデータを生成します。

## ライブラリと基本ポイント
- **libディレクトリ** : イベントポイントの計算用のライブラリと基本ポイントを記載したリストがあります。

## テストについて
- **testディレクトリ** : ライブラリの動作を外部ファイルを使って照合し、正しく動作することを検証しています。

# prsk_event_point_calc \[English]

This repository provides calculated results for event points.

## Data Format and Access Method
- **table directory**: The results can be referenced in TSV format.
- **api directory**: The results are distributed in JSON format.

## How to Generate Data
- `calc.py`: Creates data within the table directory.
- `create_json.py`: Generates data for the api directory from the data in the table directory.

## Library and Basic Points
- **lib directory**: Contains a library for event point calculations and a list detailing basic points.

## About Testing
- **test directory**: Validates the correct operation of the library by cross-referencing with external files.
