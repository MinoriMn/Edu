# Edu
* julius-4.4.2.1
* dictation-kit-v4.4
を導入下で生成・実行している。

## 実行コマンド
edu.jconfのあるディレクトリで
`$ julius -C edu.jconf -nostrip -gram dict/ForAnnouncement`
と入力すると実行できる。
`ForAnnouncement`は辞書ファイル群で
`edu.jconf`は設定ファイルである。

edu.jconfの
```
-v model/lang_m/bccwj.60k.htkdic
-h model/phone_m/jnas-tri-3k16-gid.binhmm
-hlist model/phone_m/logicalTri
```
で指定されているmodelフォルダとその内部ファイルは、dictation-kit-v4.4のmodelフォルダのことである。

## Edu_software

### ver 0.0.1a
やったこと

* 実装したEdu.pyではメイン関数系の実装を行なっているのでここから確認してください
* システムの基盤とする予定のクラスを実装しました。詳しくはスプレッドシート上のクラス構想図を参照
* 起動時のタイトルの管理を行うTitleクラス群を仮実装しました、Edu.pyよりスレッドによる呼び出しをしている。
* 実装したJulius_receiver.pyではEduソフトとjuliusの連結を行う予定。
* <span style="color: red;">※起動の際はEdu_softwareフォルダにdictation-kitのmodelフォルダを移植してください。</span>

問題点

* juliusの連結において、起動の確認まで出来ているがいくつか問題点あり。

