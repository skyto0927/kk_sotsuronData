from pydub import AudioSegment
from pydub.silence import split_on_silence

# wavファイルのデータ取得
sound = AudioSegment.from_file("recording/KaitoKobayashi/up_a.WAV", format="wav")

# wavデータの分割（無音部分で区切る）
chunks = split_on_silence(sound, min_silence_len=400, silence_thresh=-45, keep_silence=300)

#min_silence_len=2000   2000ms以上無音なら分割
#silence_thresh=-40     -40dBFS以下で無音と判定
#keep_silence=600       分割後500msは無音を残す

# 分割したデータ毎にファイルに出力
for i, chunk in enumerate(chunks):
    chunk.export("recording/KaitoKobayashi/up/output" + str(i) +".wav", format="wav")


#############################
#ファイル名の書き換えは必須！！！#
#############################