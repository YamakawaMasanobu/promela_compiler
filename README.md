# 参考サイト
* PROMELA文法
    * https://spinroot.com/spin/Man/grammar.html#ivar
* PLYリファレンス
    * https://www.dabeaz.com/ply/ply.html#ply_nn23

# 必要ファイル
* promela_compiler
    * 入力となるpmlファイル(makeファイルのTESTFILEでファイル名指定)
    * pmlparser2.py
    * edit_result_analyze.py
* PROMELA2CS内
    * gen.sh
    * Makefile
    * convartTree.erl
    * pml2cs.erl
    * setmanager.erl
* testpmlはparserのテストファイルが入ってます


# 実行方法
* ConvertedProgramでmakeする
* 入力のPROMELAファイルのプロセス名をファイル名とするerlファイルが作成される


