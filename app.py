import streamlit as st
import pandas as pd
from datetime import datetime
import io

st.set_page_config(
    page_title="生活支援技術：人生の最終段階における介護",
    page_icon="🌿",
    layout="centered"
)

# カスタムCSS（ルビの視認性とスマホ対応カードデザイン）
st.markdown("""
<style>
  ruby { ruby-align: center; }
  rt { font-size: 0.6em; color: #475569; font-weight: normal; }
  .app-header {
    background: linear-gradient(135deg, #1e3a8a, #0f766e);
    color: white;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
  }
  .app-header rt { color: #e2e8f0; }
  .app-header h1 { font-size: 1.55rem; line-height: 1.8; margin: 0; color: white; }
  .app-header p { font-size: 0.95rem; line-height: 1.8; margin-top: 8px; opacity: 0.95; }
  .info-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 5px solid #0f766e;
    border-radius: 10px;
    padding: 16px 18px;
    margin-bottom: 16px;
    line-height: 2.0;
    font-size: 1.02rem;
  }
  .case-card {
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-left: 5px solid #b45309;
    border-radius: 10px;
    padding: 16px 18px;
    margin-bottom: 16px;
    line-height: 2.05;
    font-size: 1.02rem;
  }
  .field-label {
    font-weight: bold;
    font-size: 1.05rem;
    line-height: 2.0;
    margin-top: 10px;
    margin-bottom: 4px;
    color: #1e3a8a;
  }
  table.study-tbl {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 16px;
    font-size: 0.96rem;
    line-height: 1.95;
  }
  table.study-tbl th, table.study-tbl td {
    border: 1px solid #cbd5e1;
    padding: 10px 12px;
    text-align: left;
  }
  table.study-tbl th {
    background: #f1f5f9;
    width: 28%;
    color: #1e3a8a;
  }
</style>
""", unsafe_allow_html=True)

# ヘッダー
st.markdown("""
<div class="app-header">
  <h1>🌿 <ruby>生活<rt>せいかつ</rt></ruby><ruby>支援<rt>しえん</rt></ruby><ruby>技術<rt>ぎじゅつ</rt></ruby>：<ruby>人生<rt>じんせい</rt></ruby>の<ruby>最終<rt>さいしゅう</rt></ruby><ruby>段階<rt>だんかい</rt></ruby>における<ruby>介護<rt>かいご</rt></ruby></h1>
  <p><ruby>学生用<rt>がくせいよう</rt></ruby><ruby>学習<rt>がくしゅう</rt></ruby><ruby>資料<rt>しりょう</rt></ruby> ＆ ワークシート（90<ruby>分<rt>ぷん</rt></ruby>×2コマ）</p>
</div>
""", unsafe_allow_html=True)

# 学生情報入力欄（クラス名 → 学籍番号 → 氏名の順）
st.markdown("""
<div class="info-card">
  <strong>📝 <ruby>最初<rt>さいしょ</rt></ruby>にあなたの<ruby>情報<rt>じょうほう</rt></ruby>を<ruby>入力<rt>にゅうりょく</rt></ruby>してください</strong>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="field-label">① クラス<ruby>名<rt>めい</rt></ruby></div>', unsafe_allow_html=True)
    class_name = st.text_input("class_name", label_visibility="collapsed", placeholder="例：1A")
with col2:
    st.markdown('<div class="field-label">② <ruby>学籍<rt>がくせき</rt></ruby><ruby>番号<rt>ばんごう</rt></ruby></div>', unsafe_allow_html=True)
    student_id = st.text_input("student_id", label_visibility="collapsed", placeholder="例：2026001")
with col3:
    st.markdown('<div class="field-label">③ <ruby>氏名<rt>しめい</rt></ruby></div>', unsafe_allow_html=True)
    student_name = st.text_input("student_name", label_visibility="collapsed", placeholder="例：青山 太郎")

st.divider()

# メニュー切り替え（ルビ付き案内＋番号タブ）
st.markdown("""
<div class="field-label">📚 <ruby>学習<rt>がくしゅう</rt></ruby>メニューを<ruby>選<rt>えら</rt></ruby>んでください</div>
<p style="font-size:0.92rem; line-height:1.9; color:#475569;">
【1】<ruby>資料<rt>しりょう</rt></ruby>1（エンドオブライフ・ケア） ／ 【2】ワーク1（<ruby>自分<rt>じぶん</rt></ruby>の<ruby>望<rt>のぞ</rt></ruby>み） ／ 【3】<ruby>資料<rt>しりょう</rt></ruby>2（<ruby>他者<rt>たしゃ</rt></ruby>への<ruby>支援<rt>しえん</rt></ruby>） ／ 【4】ワーク2（<ruby>事例<rt>じれい</rt></ruby><ruby>検討<rt>けんとう</rt></ruby>） ／ 【5】<ruby>提出<rt>ていしゅつ</rt></ruby>
</p>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["【1】", "【2】", "【3】", "【4】", "【5】"])

# ---------------------------------------------------------
# タブ1：第1コマ 学習資料
# ---------------------------------------------------------
with tab1:
    st.markdown("""
    <h3>📖 【<ruby>資料<rt>しりょう</rt></ruby>1】エンドオブライフ・ケアの<ruby>基本<rt>きほん</rt></ruby><ruby>理解<rt>りかい</rt></ruby>（<ruby>第<rt>だい</rt></ruby>1コマ）</h3>

    <div class="info-card">
      <strong>1. <ruby>言葉<rt>ことば</rt></ruby>の<ruby>意味<rt>いみ</rt></ruby>と<ruby>違<rt>ちが</rt></ruby>い</strong><br>
      ・<strong>ターミナルケア（<ruby>終末期<rt>しゅうまつき</rt></ruby>ケア）：</strong><ruby>主<rt>おも</rt></ruby>にがんの<ruby>末期<rt>まっき</rt></ruby>など、<ruby>余命<rt>よめい</rt></ruby>（<ruby>残<rt>のこ</rt></ruby>りの<ruby>命<rt>いのち</rt></ruby>の<ruby>時間<rt>じかん</rt></ruby>）が<ruby>数週間<rt>すうしゅうかん</rt></ruby>〜<ruby>数<rt>すう</rt></ruby>ヶ<ruby>月<rt>げつ</rt></ruby>と<ruby>短<rt>みじか</rt></ruby>い<ruby>時期<rt>じき</rt></ruby>のケア。<br>
      ・<strong><ruby>緩和<rt>かんわ</rt></ruby>ケア：</strong><ruby>重<rt>おも</rt></ruby>い<ruby>病気<rt>びょうき</rt></ruby>になった<ruby>早<rt>はや</rt></ruby>い<ruby>段階<rt>だんかい</rt></ruby>から、<ruby>体<rt>からだ</rt></ruby>や<ruby>心<rt>こころ</rt></ruby>のつらさを<ruby>和<rt>やわ</rt></ruby>らげ、<ruby>生活<rt>せいかつ</rt></ruby>の<ruby>質<rt>しつ</rt></ruby>（QOL）を<ruby>保<rt>たも</rt></ruby>つケア。<br>
      ・<strong>エンドオブライフ・ケア：</strong><ruby>病名<rt>びょうめい</rt></ruby>や<ruby>余命<rt>よめい</rt></ruby>の<ruby>長<rt>なが</rt></ruby>さに<ruby>関係<rt>かんけい</rt></ruby>なく、<ruby>老衰<rt>ろうすい</rt></ruby>や<ruby>認知症<rt>にんちしょう</rt></ruby>も<ruby>含<rt>ふく</rt></ruby>めて、<strong>「<ruby>人生<rt>じんせい</rt></ruby>の<ruby>終<rt>お</rt></ruby>わりを<ruby>意識<rt>いしき</rt></ruby>したときから、<ruby>最期<rt>さいご</rt></ruby>を<ruby>迎<rt>むか</rt></ruby>えるまで、その<ruby>人<rt>ひと</rt></ruby>らしく<ruby>生<rt>い</rt></ruby>き<ruby>抜<rt>ぬ</rt></ruby>くことを<ruby>支<rt>ささ</rt></ruby>えるケア」</strong>です。
    </div>

    <div class="info-card">
      <strong>2. <ruby>全人的<rt>ぜんじんてき</rt></ruby><ruby>苦痛<rt>くつう</rt></ruby>（トータルペイン）</strong><br>
      <ruby>人生<rt>じんせい</rt></ruby>の<ruby>最終<rt>さいしゅう</rt></ruby><ruby>段階<rt>だんかい</rt></ruby>にある<ruby>人<rt>ひと</rt></ruby>は、4つのつらさが<ruby>重<rt>かさ</rt></ruby>なり<ruby>合<rt>あ</rt></ruby>っています。<br>
      ① <strong><ruby>身体的<rt>しんたいてき</rt></ruby><ruby>苦痛<rt>くつう</rt></ruby>：</strong><ruby>痛<rt>いた</rt></ruby>み、<ruby>息苦<rt>いきぐる</rt></ruby>しさ、だるさ、<ruby>口<rt>くち</rt></ruby>の<ruby>渇<rt>かわ</rt></ruby>き、<ruby>便秘<rt>べんぴ</rt></ruby>など<br>
      ② <strong><ruby>精神的<rt>せいしんてき</rt></ruby><ruby>苦痛<rt>くつう</rt></ruby>：</strong><ruby>不安<rt>ふあん</rt></ruby>、<ruby>恐怖<rt>きょうふ</rt></ruby>、さびしさ、<ruby>怒<rt>いか</rt></ruby>りなど<br>
      ③ <strong><ruby>社会的<rt>しゃかいてき</rt></ruby><ruby>苦痛<rt>くつう</rt></ruby>：</strong><ruby>役割<rt>やくわり</rt></ruby>を<ruby>失<rt>うしな</rt></ruby>うさびしさ、お<ruby>金<rt>かね</rt></ruby>の<ruby>心配<rt>しんぱい</rt></ruby>、<ruby>家族<rt>かぞく</rt></ruby>への<ruby>気兼<rt>きが</rt></ruby>ねなど<br>
      ④ <strong>スピリチュアルペイン（<ruby>霊的<rt>れいてき</rt></ruby><ruby>苦痛<rt>くつう</rt></ruby>）：</strong>「<ruby>自分<rt>じぶん</rt></ruby>の<ruby>人生<rt>じんせい</rt></ruby>に<ruby>意味<rt>いみ</rt></ruby>はあったのか」という<ruby>深<rt>ふか</rt></ruby>い<ruby>悩<rt>なや</rt></ruby>み
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# タブ2：ワークシート1（自分にとって望ましい死）
# ---------------------------------------------------------
with tab2:
    st.markdown("""
    <h3>💭 【ワーク1】<ruby>私<rt>わたし</rt></ruby>にとって<ruby>望<rt>のぞ</rt></ruby>ましい<ruby>最期<rt>さいご</rt></ruby>を<ruby>考<rt>かんが</rt></ruby>える</h3>
    <div class="case-card">
      <strong><ruby>質問<rt>しつもん</rt></ruby>1：</strong>もし、あなたの<ruby>人生<rt>じんせい</rt></ruby>の<ruby>残<rt>のこ</rt></ruby>り<ruby>時間<rt>じかん</rt></ruby>が「あと<ruby>半年<rt>はんとし</rt></ruby>」だとしたら、<ruby>下<rt>した</rt></ruby>のA〜Jの<ruby>中<rt>なか</rt></ruby>から<strong>「<ruby>最<rt>もっと</rt></ruby>も<ruby>大切<rt>たいせつ</rt></ruby>にしたいこと」を3つ</strong><ruby>選<rt>えら</rt></ruby>んでください。（<ruby>正解<rt>せいかい</rt></ruby>はありません）<br><br>
      ・<strong>A：</strong><ruby>痛<rt>いた</rt></ruby>みや<ruby>苦<rt>くる</rt></ruby>しみがないこと<br>
      ・<strong>B：</strong><ruby>最期<rt>さいご</rt></ruby>まで<ruby>自分<rt>じぶん</rt></ruby>の<ruby>頭<rt>あたま</rt></ruby>で<ruby>考<rt>かんが</rt></ruby>え、<ruby>判断<rt>はんだん</rt></ruby>できること<br>
      ・<strong>C：</strong><ruby>家族<rt>かぞく</rt></ruby>や<ruby>大切<rt>たいせつ</rt></ruby>な<ruby>人<rt>ひと</rt></ruby>と<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>過<rt>す</rt></ruby>ごす<ruby>時間<rt>じかん</rt></ruby>を<ruby>持<rt>も</rt></ruby>つこと<br>
      ・<strong>D：</strong><ruby>家族<rt>かぞく</rt></ruby>に<ruby>介護<rt>かいご</rt></ruby>やお<ruby>金<rt>かね</rt></ruby>の<ruby>負担<rt>ふたん</rt></ruby>をかけないこと<br>
      ・<strong>E：</strong><ruby>住<rt>す</rt></ruby>み<ruby>慣<rt>な</rt></ruby>れた<ruby>自宅<rt>じたく</rt></ruby>（<ruby>自分<rt>じぶん</rt></ruby>の<ruby>部屋<rt>へや</rt></ruby>）で<ruby>過<rt>す</rt></ruby>ごすこと<br>
      ・<strong>F：</strong><ruby>医師<rt>いし</rt></ruby>や<ruby>設備<rt>せつび</rt></ruby>が<ruby>整<rt>ととの</rt></ruby>った<ruby>病院<rt>びょういん</rt></ruby>で<ruby>安心<rt>あんしん</rt></ruby>して<ruby>過<rt>す</rt></ruby>ごすこと<br>
      ・<strong>G：</strong><ruby>最期<rt>さいご</rt></ruby>まで<ruby>好<rt>す</rt></ruby>きなものを<ruby>口<rt>くち</rt></ruby>から<ruby>食<rt>た</rt></ruby>べること<br>
      ・<strong>H：</strong>トイレやお<ruby>風呂<rt>ふろ</rt></ruby>など、<ruby>人<rt>ひと</rt></ruby>の<ruby>手<rt>て</rt></ruby>を<ruby>借<rt>か</rt></ruby>りずに<ruby>自分<rt>じぶん</rt></ruby>でできること<br>
      ・<strong>I：</strong><ruby>自分<rt>じぶん</rt></ruby>の<ruby>趣味<rt>しゅみ</rt></ruby>ややりたいことを<ruby>最期<rt>さいご</rt></ruby>まで<ruby>続<rt>つづ</rt></ruby>けること<br>
      ・<strong>J：</strong>その<ruby>他<rt>ほか</rt></ruby>（<ruby>自由<rt>じゆう</rt></ruby>に<ruby>考<rt>かんが</rt></ruby>える）
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="field-label">▼ A〜Jから3つ<ruby>選<rt>えら</rt></ruby>んでチェックしてください</div>', unsafe_allow_html=True)
    w1_choices = st.multiselect(
        "w1_choices",
        options=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        max_selections=3,
        label_visibility="collapsed"
    )

    st.markdown('<div class="field-label">▼ <ruby>質問<rt>しつもん</rt></ruby>2：その3つを<ruby>選<rt>えら</rt></ruby>んだ<ruby>理由<rt>りゆう</rt></ruby>を<ruby>書<rt>か</rt></ruby>いてみましょう</div>', unsafe_allow_html=True)
    w1_reason = st.text_area("w1_reason", height=100, label_visibility="collapsed")

    st.markdown('<div class="field-label">▼ <ruby>質問<rt>しつもん</rt></ruby>3：グループで<ruby>話<rt>はな</rt></ruby>し<ruby>合<rt>あ</rt></ruby>って<ruby>気<rt>き</rt></ruby>づいたこと（<ruby>自分<rt>じぶん</rt></ruby>と<ruby>同<rt>おな</rt></ruby>じところ・<ruby>違<rt>ちが</rt></ruby>うところ）</div>', unsafe_allow_html=True)
    w1_reflection = st.text_area("w1_reflection", height=100, label_visibility="collapsed")

# ---------------------------------------------------------
# タブ3：第2コマ 学習資料
# ---------------------------------------------------------
with tab3:
    st.markdown("""
    <h3>🤝 【<ruby>資料<rt>しりょう</rt></ruby>2】<ruby>他者<rt>たしゃ</rt></ruby>の<ruby>望<rt>のぞ</rt></ruby>ましい<ruby>死<rt>し</rt></ruby>を<ruby>支<rt>ささ</rt></ruby>えるACPと<ruby>生活<rt>せいかつ</rt></ruby><ruby>支援<rt>しえん</rt></ruby><ruby>技術<rt>ぎじゅつ</rt></ruby>（<ruby>第<rt>だい</rt></ruby>2コマ）</h3>

    <div class="info-card">
      <strong>1. ACP（アドバンス・ケア・プランニング／<ruby>人生<rt>じんせい</rt></ruby><ruby>会議<rt>かいぎ</rt></ruby>）と<ruby>介護<rt>かいご</rt></ruby><ruby>福祉士<rt>ふくしし</rt></ruby>の<ruby>役割<rt>やくわり</rt></ruby></strong><br>
      ・<ruby>利用者<rt>りようしゃ</rt></ruby>が<ruby>望<rt>のぞ</rt></ruby>む<ruby>医療<rt>いりょう</rt></ruby>や<ruby>生活<rt>せいかつ</rt></ruby>について、<ruby>本人<rt>ほんにん</rt></ruby>・<ruby>家族<rt>かぞく</rt></ruby>・<ruby>専門職<rt>せんもんしょく</rt></ruby>で<strong><ruby>繰<rt>く</rt></ruby>り<ruby>返<rt>かえ</rt></ruby>し<ruby>話<rt>はな</rt></ruby>し<ruby>合<rt>あ</rt></ruby>う</strong>こと。<br>
      ・<ruby>介護<rt>かいご</rt></ruby><ruby>福祉士<rt>ふくしし</rt></ruby>は、<ruby>毎日<rt>まいにち</rt></ruby>のケアの<ruby>中<rt>なか</rt></ruby>で<ruby>見<rt>み</rt></ruby>える「<ruby>好<rt>す</rt></ruby>きな<ruby>食<rt>た</rt></ruby>べ<ruby>物<rt>もの</rt></ruby>」「<ruby>心地<rt>ここち</rt></ruby>よさそうな<ruby>表情<rt>ひょうじょう</rt></ruby>」「ふとした<ruby>言葉<rt>ことば</rt></ruby>」を<ruby>記録<rt>きろく</rt></ruby>し、チームに<ruby>伝<rt>つた</rt></ruby>えます。<br>
      ・<ruby>一度<rt>いちど</rt></ruby><ruby>決<rt>き</rt></ruby>めた<ruby>気持<rt>きも</rt></ruby>ちも、<ruby>体調<rt>たいちょう</rt></ruby>が<ruby>変<rt>か</rt></ruby>われば<strong>「<ruby>揺<rt>ゆ</rt></ruby>れ<ruby>動<rt>うご</rt></ruby>く（<ruby>迷<rt>まよ</rt></ruby>う）」のが<ruby>自然<rt>しぜん</rt></ruby></strong>です。
    </div>

    <table class="study-tbl">
      <tr>
        <th><ruby>食事<rt>しょくじ</rt></ruby>・<ruby>口腔<rt>こうくう</rt></ruby>ケア</th>
        <td><ruby>飲<rt>の</rt></ruby>み<ruby>込<rt>こ</rt></ruby>む<ruby>力<rt>ちから</rt></ruby>（<ruby>嚥下<rt>えんげ</rt></ruby><ruby>機能<rt>きのう</rt></ruby>）が<ruby>弱<rt>よわ</rt></ruby>くなったら、<ruby>無理<rt>むり</rt></ruby>に<ruby>食<rt>た</rt></ruby>べさせず、<ruby>看護師<rt>かんごし</rt></ruby>と<ruby>相談<rt>そうだん</rt></ruby>して<ruby>好物<rt>こうぶつ</rt></ruby>の<ruby>香<rt>かお</rt></ruby>りや<ruby>味<rt>あじ</rt></ruby>で<ruby>唇<rt>くちびる</rt></ruby>を<ruby>潤<rt>うるお</rt></ruby>す。<ruby>口<rt>くち</rt></ruby>の<ruby>中<rt>なか</rt></ruby>を<ruby>清潔<rt>せいけつ</rt></ruby>にし、<ruby>保湿<rt>ほしつ</rt></ruby>ジェルで<ruby>乾燥<rt>かんそう</rt></ruby>を<ruby>防<rt>ふせ</rt></ruby>ぐ。</td>
      </tr>
      <tr>
        <th><ruby>清潔<rt>せいけつ</rt></ruby>・<ruby>排泄<rt>はいせつ</rt></ruby></th>
        <td>お<ruby>風呂<rt>ふろ</rt></ruby>で<ruby>疲<rt>つか</rt></ruby>れるときは、<ruby>温<rt>あたた</rt></ruby>かいタオルでの<ruby>清拭<rt>せいしき</rt></ruby>（<ruby>体<rt>からだ</rt></ruby>を<ruby>拭<rt>ふ</rt></ruby>く）や<ruby>足浴<rt>そくよく</rt></ruby>・<ruby>手浴<rt>しゅよく</rt></ruby>にする。おむつ<ruby>交換<rt>こうかん</rt></ruby>は<ruby>恥<rt>は</rt></ruby>ずかしさに<ruby>配慮<rt>はいりょ</rt></ruby>し、<ruby>皮膚<rt>ひふ</rt></ruby>を<ruby>優<rt>やさ</rt></ruby>しく<ruby>守<rt>まも</rt></ruby>る。</td>
      </tr>
      <tr>
        <th><ruby>安楽<rt>あんらく</rt></ruby>・<ruby>環境<rt>かんきょう</rt></ruby></th>
        <td>クッションで<ruby>息<rt>いき</rt></ruby>がしやすい<ruby>姿勢<rt>しせい</rt></ruby>（ポジショニング）をつくる。<ruby>耳<rt>みみ</rt></ruby>（<ruby>聴覚<rt>ちょうかく</rt></ruby>）は<ruby>最期<rt>さいご</rt></ruby>まで<ruby>聞<rt>き</rt></ruby>こえるため、<ruby>優<rt>やさ</rt></ruby>しい<ruby>声<rt>こえ</rt></ruby>かけと<ruby>好<rt>す</rt></ruby>きな<ruby>音楽<rt>おんがく</rt></ruby>で<ruby>穏<rt>おだ</rt></ruby>やかな<ruby>空間<rt>くうかん</rt></ruby>をつくる。</td>
      </tr>
      <tr>
        <th><ruby>家族<rt>かぞく</rt></ruby>ケア・<ruby>死後<rt>しご</rt></ruby>のケア</th>
        <td><ruby>家族<rt>かぞく</rt></ruby>も「<ruby>何<rt>なに</rt></ruby>かしてあげたい」と<ruby>悩<rt>なや</rt></ruby>んでいる。<ruby>手<rt>て</rt></ruby>のマッサージや<ruby>口<rt>くち</rt></ruby>の<ruby>保湿<rt>ほしつ</rt></ruby>などを<ruby>家族<rt>かぞく</rt></ruby>と<ruby>一緒<rt>いっしょ</rt></ruby>に<ruby>行<rt>おこな</rt></ruby>う。<ruby>亡<rt>な</rt></ruby>くなった<ruby>後<rt>あと</rt></ruby>のエンゼルケアも<ruby>家族<rt>かぞく</rt></ruby>の<ruby>気持<rt>きも</rt></ruby>ちに<ruby>寄<rt>よ</rt></ruby>り<ruby>添<rt>そ</rt></ruby>って<ruby>丁寧<rt>ていねい</rt></ruby>に<ruby>行<rt>おこな</rt></ruby>う。</td>
      </tr>
    </table>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# タブ4：ワークシート2（事例検討）
# ---------------------------------------------------------
with tab4:
    st.markdown("""
    <h3>🏥 【ワーク2】<ruby>事例<rt>じれい</rt></ruby><ruby>検討<rt>けんとう</rt></ruby>：<ruby>他者<rt>たしゃ</rt></ruby>にとって<ruby>望<rt>のぞ</rt></ruby>ましい<ruby>最期<rt>さいご</rt></ruby>を<ruby>支<rt>ささ</rt></ruby>える</h3>
    <div class="case-card">
      <strong>【<ruby>事例<rt>じれい</rt></ruby>】Aさん（88<ruby>歳<rt>さい</rt></ruby>・<ruby>女性<rt>じょせい</rt></ruby>・<ruby>要介護<rt>ようかいご</rt></ruby>5・アルツハイマー<ruby>型<rt>がた</rt></ruby><ruby>認知症<rt>にんちしょう</rt></ruby>・<ruby>老衰<rt>ろうすい</rt></ruby>）</strong><br>
      <ruby>特別<rt>とくべつ</rt></ruby><ruby>養護<rt>ようご</rt></ruby><ruby>老人<rt>ろうじん</rt></ruby>ホームに<ruby>入所<rt>にゅうしょ</rt></ruby>して4<ruby>年<rt>ねん</rt></ruby>になります。<ruby>以前<rt>いぜん</rt></ruby>は<ruby>歌<rt>うた</rt></ruby>が<ruby>好<rt>す</rt></ruby>きで、おやつの<ruby>時間<rt>じかん</rt></ruby>には<ruby>大好き<rt>だいすき</rt></ruby>な<strong><ruby>抹茶<rt>まっちゃ</rt></ruby>と<ruby>羊羹<rt>ようかん</rt></ruby></strong>を<ruby>笑顔<rt>えがお</rt></ruby>で<ruby>食<rt>た</rt></ruby>べていました。<br>
      1ヶ<ruby>月前<rt>げつまえ</rt></ruby>から<ruby>食事<rt>しょくじ</rt></ruby>の<ruby>量<rt>りょう</rt></ruby>が<ruby>急<rt>きゅう</rt></ruby>に<ruby>減<rt>へ</rt></ruby>り、<ruby>今<rt>いま</rt></ruby>は<ruby>一日<rt>いちにち</rt></ruby>の<ruby>大半<rt>たいはん</rt></ruby>を<ruby>眠<rt>ねむ</rt></ruby>って<ruby>過<rt>す</rt></ruby>ごしています。<ruby>飲<rt>の</rt></ruby>み<ruby>込<rt>こ</rt></ruby>む<ruby>力<rt>ちから</rt></ruby>が<ruby>弱<rt>よわ</rt></ruby>くなり、<ruby>水分<rt>すいぶん</rt></ruby>でむせることが<ruby>増<rt>ふ</rt></ruby>えました。<br>
      <ruby>入所<rt>にゅうしょ</rt></ruby>したとき、<ruby>本人<rt>ほんにん</rt></ruby>も<ruby>長女<rt>ちょうじょ</rt></ruby>（60<ruby>歳<rt>さい</rt></ruby>）も「<ruby>無理<rt>むり</rt></ruby>な<ruby>延命<rt>えんめい</rt></ruby><ruby>治療<rt>ちりょう</rt></ruby>はせず、<ruby>施設<rt>しせつ</rt></ruby>で<ruby>穏<rt>おだ</rt></ruby>やかに<ruby>最期<rt>さいご</rt></ruby>を<ruby>迎<rt>むか</rt></ruby>えたい」と<ruby>希望<rt>きぼう</rt></ruby>していました。<br>
      しかし<ruby>今日<rt>きょう</rt></ruby>、<ruby>面会<rt>めんかい</rt></ruby>に<ruby>来<rt>き</rt></ruby>た<ruby>長女<rt>ちょうじょ</rt></ruby>が、<ruby>痩<rt>や</rt></ruby>せて<ruby>眠<rt>ねむ</rt></ruby>り<ruby>続<rt>つづ</rt></ruby>けるAさんを<ruby>見<rt>み</rt></ruby>て<ruby>涙<rt>なみだ</rt></ruby>ぐみ、<br>
      <strong>「こんなに<ruby>食<rt>た</rt></ruby>べられないなら、やっぱり<ruby>病院<rt>びょういん</rt></ruby>に<ruby>入院<rt>にゅういん</rt></ruby>させて<ruby>点滴<rt>てんてき</rt></ruby>してもらった<ruby>方<rt>ほう</rt></ruby>がいいのでしょうか…<ruby>見殺<rt>みごろ</rt></ruby>しにしているみたいでつらいです」</strong><br>
      と、<ruby>担当<rt>たんとう</rt></ruby><ruby>介護<rt>かいご</rt></ruby><ruby>福祉士<rt>ふくしし</rt></ruby>のあなたに<ruby>話<rt>はな</rt></ruby>しかけてきました。
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="field-label">▼ <ruby>課題<rt>かだい</rt></ruby>1：<ruby>長女<rt>ちょうじょ</rt></ruby>は<ruby>今<rt>いま</rt></ruby>、どのような<ruby>気持<rt>きも</rt></ruby>ち（<ruby>不安<rt>ふあん</rt></ruby>や<ruby>迷<rt>まよ</rt></ruby>い）を<ruby>抱<rt>かか</rt></ruby>えていると<ruby>考<rt>かんが</rt></ruby>えられますか？</div>', unsafe_allow_html=True)
    w2_q1 = st.text_area("w2_q1", height=95, label_visibility="collapsed")

    st.markdown('<div class="field-label">▼ <ruby>課題<rt>かだい</rt></ruby>2：<ruby>長女<rt>ちょうじょ</rt></ruby>に<ruby>最初<rt>さいしょ</rt></ruby>にどのような<ruby>声<rt>こえ</rt></ruby>をかけますか？また、どの<ruby>専門職<rt>せんもんしょく</rt></ruby>（<ruby>医師<rt>いし</rt></ruby>・<ruby>看護師<rt>かんごし</rt></ruby>など）とどう<ruby>連携<rt>れんけい</rt></ruby>しますか？</div>', unsafe_allow_html=True)
    w2_q2 = st.text_area("w2_q2", height=95, label_visibility="collapsed")

    st.markdown('<div class="field-label">▼ <ruby>課題<rt>かだい</rt></ruby>3：Aさんが「Aさんらしく」<ruby>心地<rt>ここち</rt></ruby>よく<ruby>過<rt>す</rt></ruby>ごし、<ruby>長女<rt>ちょうじょ</rt></ruby>も<ruby>安心<rt>あんしん</rt></ruby>して<ruby>寄<rt>よ</rt></ruby>り<ruby>添<rt>そ</rt></ruby>えるように、どのような「<ruby>生活<rt>せいかつ</rt></ruby><ruby>支援<rt>しえん</rt></ruby><ruby>技術<rt>ぎじゅつ</rt></ruby>」を<ruby>工夫<rt>くふう</rt></ruby>しますか？</div>', unsafe_allow_html=True)
    w2_q3 = st.text_area("w2_q3", height=110, label_visibility="collapsed")

# ---------------------------------------------------------
# タブ5：確認・提出用ファイルダウンロード
# ---------------------------------------------------------
with tab5:
    st.markdown("""
    <h3>📤 <ruby>回答<rt>かいとう</rt></ruby>の<ruby>確認<rt>かくにん</rt></ruby>と<ruby>提出用<rt>ていしゅつよう</rt></ruby>ファイルの<ruby>保存<rt>ほぞん</rt></ruby></h3>
    <div class="info-card">
      クラス<ruby>名<rt>めい</rt></ruby>・<ruby>学籍<rt>がくせき</rt></ruby><ruby>番号<rt>ばんごう</rt></ruby>・<ruby>氏名<rt>しめい</rt></ruby>と、ワーク1・ワーク2の<ruby>入力<rt>にゅうりょく</rt></ruby>が<ruby>終<rt>お</rt></ruby>わったら、<ruby>下<rt>した</rt></ruby>のボタンからCSVファイルを<ruby>保存<rt>ほぞん</rt></ruby>して<ruby>先生<rt>せんせい</rt></ruby>の<ruby>指示<rt>しじ</rt></ruby>どおりに<ruby>提出<rt>ていしゅつ</rt></ruby>してください。
    </div>
    """, unsafe_allow_html=True)

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    df_submit = pd.DataFrame([{
        "提出日時": now_str,
        "クラス名": class_name,
        "学籍番号": student_id,
        "氏名": student_name,
        "ワーク1_選択項目": " / ".join(w1_choices),
        "ワーク1_選んだ理由": w1_reason,
        "ワーク1_グループの気づき": w1_reflection,
        "ワーク2_課題1_長女の気持ち": w2_q1,
        "ワーク2_課題2_声かけと連携": w2_q2,
        "ワーク2_課題3_生活支援技術": w2_q3,
    }])

    if not (class_name and student_id and student_name):
        st.markdown("""
        <div class="case-card">
          ⚠️ <ruby>画面<rt>がめん</rt></ruby>の<ruby>一番上<rt>いちばんうえ</rt></ruby>にある「①クラス<ruby>名<rt>めい</rt></ruby>」「②<ruby>学籍<rt>がくせき</rt></ruby><ruby>番号<rt>ばんごう</rt></ruby>」「③<ruby>氏名<rt>しめい</rt></ruby>」をすべて<ruby>入力<rt>にゅうりょく</rt></ruby>してください。
        </div>
        """, unsafe_allow_html=True)
    else:
        csv_buf = io.StringIO()
        df_submit.to_csv(csv_buf, index=False, encoding="utf-8-sig")
        safe_id = student_id.strip() or "student"
        file_name = f"eol_care_{class_name}_{safe_id}.csv"

        st.markdown('<div class="field-label">▼ <ruby>下<rt>した</rt></ruby>のボタンをおして<ruby>保存<rt>ほぞん</rt></ruby>（ダウンロード）</div>', unsafe_allow_html=True)
        st.download_button(
            label="📥 CSVダウンロード",
            data=csv_buf.getvalue().encode("utf-8-sig"),
            file_name=file_name,
            mime="text/csv"
        )