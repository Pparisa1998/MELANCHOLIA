# Thesis game
# ยังไม่ได้ใส่รูปกับเสียงท้ายบท #
# ประกาศตัวแปรก่อนใช้งาน
define chin = Character("เตชิน", color="#3A84BE")
define r = Character("ศรัน", color="#d23edf")
define l = Character("ลิน", color="#3abe80")
define npc = Character("เมย์", color="#ff89a7")
define b = Character("ปุณ", color="#f7a52a")
define attention = Character("ประกาศ", color="#000000")
define vdo = Character("คลิปวีดีโอ", color="#000000")
default score = 0

# บทที่ 1
label start:  # The game starts here.

    play music "bgm.mp3" loop
    $ renpy.music.set_volume(0.25, channel="music")
    
    show start1
    pause 10.0
    hide start1
    
    scene bg school front with dissolve

    # ตั้งค่าเสียงให้ดังสุดก่อน
    $ renpy.music.set_volume(1.0, channel="sound")

    # เล่นเสียงประกาศ
    play sound "1atten.mp3"
    
    # เว้นจังหวะให้เสียงได้เล่นเต็มก่อน
    $ renpy.pause(0.5)

    attention "สวัสดีน้อง ๆ นักศึกษาปี 1 ทุกคนนะคะ กิจกรรมในวันนี้ทางสโมสรนักศึกษาฯ \
ขอให้น้อง ๆ ปี 1 เตรียมตัวเข้าร่วมกิจกรรมด้วยการจับกลุ่ม จำนวนกลุ่มละ 5 คนไม่จำกัดเพศ \
แต่มีเงื่อนไขว่าให้คละคณะ เพื่อให้น้อง ๆ ได้ทำความรู้จักเพื่อน ๆ จากคณะอื่น \
เมื่อเรียบร้อยแล้วจะมีพี่ ๆ นำแถวเข้าไปในอาคารค่ะ ขอบคุณค่ะ"

    stop sound fadeout 0.5
    
    show player bl
    b "เอ่อ… กลุ่มเธอครบรึยัง ? พวกเราขออยู่ด้วยได้ไหม ?" 
    hide player bl
    
    show depress1r
    play sound "1t1.mp3"
    chin "ได้ครับ"
    hide depress1r

    show depress3
    play sound "1r1.mp3"
    r "ได้สิกลุ่มเราขาด 2 คนพอดีเลย"
    hide depress3
    stop sound

    show npcc
    play sound "1m1.mp3"
    npc "ดีเลย! พวกเธอชื่ออะไรกันเหรอ ?"
    stop sound
    play sound "1m2.mp3"
    npc "เราชื่อเมย์นะ อยู่คณะวิทย์ "
    hide npcc
    stop sound

    show player bc
    b "เราชื่อ ' ปุณ ' คณะวิทย์เหมือนกัน ยินดีที่ได้รู้จักนะ ! "
    hide player bc
    
    show depress1
    play sound "1_t2.mp3"
    chin "เราชื่อ ชิน คณะแพทย์ "
    hide depress1
    stop sound

    show depress22
    play sound "1l1.mp3"
    l "เราชื่อลิน...อยู่ศิลปกรรม"
    hide depress22
    stop sound

    show depress3
    play sound "1r2.mp3"
    r "เราศรัน เรียกรันก็ได้ เรียนวิศวะ"
    hide depress3
    stop sound
    
    show player bc
    b "เราเห็นเธอคล้องป้ายชื่อกัน 
    \nเรากับเมย์ยังไม่ได้เลยไปเอาป้ายชื่อที่ไหนเหรอ พาเราไปได้ไหม"
    hide player bc

label yard_1:
    scene bg yard at Transform(zoom=3.5) with dissolve
    show depress1 
    play sound "1_t3.mp3"
    chin "เธอเข้าไปลงทะเบียนเถอะ เรารอตรงนี้"
    hide depress1
    stop sound

    show player bc
    b "รอเราแป๊บนะ"
    hide player bc
    
    define s1 = Character("พี่สโมสรนักศึกษา 1", color="#c13474")
    define s2 = Character("พี่สโมสรนักศึกษา 2", color="#c13474")
    show s1  #สโม 1
    play sound "1smo11.mp3"
    s1 "สวัสดีค่ะ ลงทะเบียนกับรับป้ายชื่อใช่ไหมคะ? "
    stop sound

    show player br
    b "ใช่ครับ"
    hide player br 

    show s2  #สโม 2
    play sound "1smo21.mp3"
    s2 "เอ่อ … ผู้ชายที่เดินมาด้วยกัน เป็นเพื่อนกันเหรอ ?"
    stop sound

    show npcr  #npc
    play sound "1m3.mp3"
    npc "ใช่ค่ะ เป็นเพื่อนที่อยู่กลุ่มเดียวกัน พี่รู้จักชินด้วยเหรอคะ"
    hide npcr
    stop sound
    
    play sound "1smo12.mp3"
    s1 "เธอก็รู้จักเตชินด้วยเหรอ ?"
    stop sound
    play sound "1smo22.mp3"
    s2 "เตชิน อนุสรณ์สกุล ไง ถ้าตามข่าวการเมืองก็ต้องรู้จักแหละ "
    stop sound
    play sound "1smo13.mp3"
    s1 "อือ ก็ลูกชายของนักการเมือง"
    stop sound
    play sound "1smo23.mp3"
    s2 "นั่นแหละ แต่ปีที่แล้วเขาเข้าโบราณคดีที่อื่นนี่นา ทำไมถึงกลายเป็นน้องใหม่ที่นี่ได้ล่ะ ?"
    stop sound
    play sound "1smo14.mp3"
    s1 "ซิ่วมาล่ะมั้ง แต่เราว่าเขาดูแปลก ๆ อะ"
    stop sound
    play sound "1smo24.mp3"
    s2 "แปลกยังไง?"
    stop sound
    play sound "1smo15.mp3" 
    s1 "ก็ขนาดแม่ตัวเองเสีย คนรู้กันทั้งเมือง มีข่าวลือว่าเขาไม่ไปงานศพเนี่ยสิ"
    hide s1
    hide s2
    stop sound

    show depress1
    play sound "1_t4.mp3"
    chin "พวกเธอเสร็จหรือยัง ?"
    hide depress1
    stop sound

    show player bc
    b "เสร็จแล้ว เรากลับไปหาเพื่อนกันเถอะ"
    hide player bc
    show black with Fade(0.5, 0.5, 0.5)
    play sound "1sup_3.mp3"
    "เตชินนึกถึงประโยคเมื่อสักครู่ “ คนรู้กันทั้งเมือง แต่ดันมีข่าวลือว่าเขาไม่ไปงานศพ ... ” 
    \nทำให้ภาพเหตุการณ์ในอดีตย้อนกลับมา"
    stop sound
    hide black

    # cut scene 1
    scene fb1 with Fade(0.5, 0.5, 0.5)
    define aj = Character("อาจารย์", color="#291c70")
    define dad = Character("พ่อของเตชิน", color="#291c70")
    define mom = Character("แม่ของเตชิน", color="#000000")
    play sound "cs1sup_1.mp3"
    "หน้าพักห้องอาจารย์สาขาโบราณคดี เตชินยืนสีหน้าเรียบนิ่งแต่แววตาเต็มไปด้วยความลังเล 
    \nเขาถือเอกสารลาออกแน่น ก่อนค่อย ๆ ยื่นให้กับอาจารย์ที่ปรึกษา"
    play sound "อาจารย์_1.mp3"
    aj "คุณตัดสินใจดีแล้วใช่ไหม ? 
    \nคุณดูมีความสุขกับการเรียนที่นี่นะ ปรึกษาผู้ปกครองรึยัง ?"
    stop sound
    play sound "cs1 t1.mp3"
    chin "ครับ ผมตัดสินใจแล้ว ที่บ้านอยากให้ผมเรียนหมอครับ"
    stop sound

    scene fb2 with Fade(0.5, 0.0, 0.5)
    play sound "cs1sup_2.mp3"
    "ณ บ้านของเตชิน เมื่อเดินเข้ามาภายในบ้านแม่ของเขานั่งพักผ่อนอยู่บนโซฟา สีหน้าอ่อนแรง "
    stop sound
    play sound "cs1 t2.mp3"
    chin "แม่ครับ... ทำไมไม่บอกผมว่าแม่ป่วย ?"
    stop sound
    play sound "แม่ไม่อยากให้ลูกกังวล.mp3"
    mom "แม่ไม่อยากให้ลูกกังวล"
    stop sound
    play sound "cs1 t3.mp3"
    chin "แล้วพ่อ..."
    stop sound
    play sound "ไม่ใช่ความผิดของพ่อ 1.mp3"
    mom "ไม่ใช่ความผิดของพ่อ
    \nพ่อกับแม่คุยกันแล้วว่าจะไม่บอกลูก"
    stop sound
    play sound "ไม่ใช่ความผิดของพ่อ 2.mp3"
    mom "พ่ออยากให้ลูกให้ความสำคัญกับเรื่องเรียนก่อน"
    stop sound
    play sound "ไม่ใช่ความผิดของพ่อ 3.mp3"
    mom "พ่อเขาหวังดีเขาอยากให้ลูกมีอนาคตที่มั่นคงนะลูก"
    stop sound
    play sound "cs1 t4.mp3"
    chin "แต่แม่คือคนสำคัญที่สุดสำหรับผม..."
    stop sound

    scene fb3 with Fade(0.5, 0.0, 0.5)
    play sound "cs1sup_3.mp3"
    "กองหนังสือที่วางซ้อนกันอยู่เต็มโต๊ะ เตชินอ่านอย่างเคร่งเครียด มือกำปากกาแน่น 
    \nสายตาเหลือบมองโทรศัพท์บ่อยครั้ง แต่ไม่มีข้อความจากแม่ เขาพยายามโทรหาแม่ 
    \nแต่ปลายสายตัดไปทุกครั้ง"
    stop sound

    scene fb4 with Fade(0.5, 0.0, 0.5)
    play sound "cs1sup_4.mp3"
    "วันสอบ เตชินได้รับโทรศัพท์จากพ่อ มีเสียงแม่แว่วมาเบา ๆ มาในโทรศัพท์ ก่อนสายถูกตัดไป"
    stop sound 
    play sound "cs1 dad_1.mp3"
    dad "โทรศัพท์ : แกต้องตั้งใจสอบ อย่าให้เรื่องอื่นมารบกวน"
    stop sound
    play sound "cs1 t5.mp3"
    chin "แล้วแม่ล่ะครับ ? "
    stop sound
    play sound "cs1 dad_2.mp3"
    dad "แม่แกต้องพักผ่อน อย่าทำให้แม่เป็นห่วงด้วยเรื่องไม่เป็นเรื่อง"
    stop sound

    scene fb5 with Fade(0.5, 0.0, 0.5)
    play sound "cs1sup_5.mp3"
    "เตชินเลื่อนเมาส์ไปกดรีเฟรชหน้าเว็บไซต์ประกาศผลสอบ หัวใจเต้นแรง สายตาจับจ้องไปยังรายชื่อที่ไล่เรียงกันยาว
    \n      เตชิน อนุสรณ์สกุล – คณะแพทยศาสตร์
    \nเขานั่งนิ่งอยู่หน้าจอครู่หนึ่ง ก่อนรีบหยิบโทรศัพท์ขึ้นมากดโทรหาแม่ แต่ปลายสายไม่มีเสียงตอบรับ "
    stop sound

    scene fb6 with Fade(0.5, 0.0, 0.5)
    play sound "cs1sup_6.mp3"
    "พ่อพาเขามาที่สุสาน เตชินชะงักเมื่อเห็นชื่อแม่สลักอยู่บนป้ายหิน"
    stop sound
    play sound "cs1 t6.mp3"
    chin "ทำไมพ่อไม่บอกผม...?"
    stop sound
    play sound "cs1 dad_3.mp3"
    dad "แม่ไม่อยากให้ลูกเสียสมาธิก่อนสอบ"
    stop sound
    play sound "cs1 t7.mp3"
    chin "แม่ไม่อยาก หรือพ่อไม่อยากกันแน่ ?"
    stop sound
    play sound "cs1 dad_4.mp3"
    dad "(พ่อชูสมุดบันทึกในมือ) นี่คือสิ่งที่แม่เขียนถึงแกทั้งหมด"
    stop sound
    play sound "cs1 dad_5.mp3"
    dad "แกจะได้อ่านมัน ก็ต่อเมื่อเรียนจบแพทย์เท่านั้น"
    stop sound


# บทที่ 2
label grass:
    scene bg yard at Transform(zoom=3.5) with dissolve
    play sound "2sup1.mp3"
    "เสียงผู้คนที่เข้าร่วมกิจกรรมดึงเตชินออกจากความคิด"
    stop sound
    show player bl
    b "ชิน ! ชิน ! เป็นอะไรหรือเปล่า ?"
    show depress1r
    play sound "2t1.mp3"
    chin "... ผมไม่เป็นไรครับ"
    stop sound
    hide player bl
    hide depress1r

label sport:
    scene bg sport hall
    play sound "2sup2.mp3"
    "ลานหน้าอาคารกิจกรรมเต็มไปด้วย นักศึกษาปี 1 กำลังต่อแถวลงทะเบียน 
    \nเสียงพูดคุยจอแจดังทั่วบริเวณ แดดช่วงสายเริ่มแรงขึ้นเรื่อย ๆ "
    stop sound
    show npcc
    play sound "2m1.mp3"
    npc "โห คนเยอะกว่าที่คิดนะเนี่ยะ นี่พวกเรามาสายไปหรือเปล่า ?"
    stop sound
    show depress1r
    chin "..."
    play sound "2m2.mp3"
    npc "ขอบใจนะชินที่เดินมาเป็นเพื่อนเรา"
    stop sound
    chin "..."
    play sound "2m3.mp3"
    npc "แต่ก็ไม่ใช่ทุกคนที่ชอบบรรยากาศแบบนี้อะเนอะ…"
    stop sound
    show player bl
    b "อืม..."
    hide npcc
    hide player bl
    hide depress1r
    menu:
        "เอ่อออ ... เธอไม่เป็นไรใช่ไหม ? ":
            show depress1c
            play sound "2tQ1_0.mp3"
            chin "...อืม"
            stop sound
            hide depress1c
            jump question_2_2

        "เป็นอะไร ทำไมทำหน้าเครียดขนาดนั้น ? แค่งานรับน้องเอง ":
            show depress1ca
            play sound "2tQ1_-1.mp3"
            chin "เราไม่ได้เป็นอะไร"
            stop sound
            hide depress1ca
            jump question_2_4

        "ชินเป็นอะไรรึเปล่า ? สีหน้าเธอไม่ค่อยดีเลยนะ เราย้ายไปตรงที่คนน้อยกว่านี้กันไหม ? ":
            show depress1smilec
            play sound "2tQ1_+1.mp3"
            chin "อืม ... ก็ดีเหมือนกัน"
            stop sound
            hide depress1smilec
            jump question_2_2


label question_2_2:
    menu:
        "มีเรื่องไม่สบายใจรึเปล่า ? ":
            show depress1smilec
            play sound "2tQ2_+1.mp3"
            chin "อืม ... ประมาณนั้น"
            stop sound
            hide depress1smilec
            jump question_2_3

        "เธอไม่ค่อยชอบกิจกรรมกลุ่มแบบนี้เหรอ ? ":
            show depress1c
            play sound "2tQ2_0.mp3"
            chin "ก็...ประมาณนั้น"
            stop sound
            hide depress1c
            jump question_2_3

        "ทำตัวปกติหน่อยไม่ได้เหรอ?":
            show depress1ca
            play sound "2tQ2_-1.mp3"
            chin "เราก็ไม่อยากเป็นแบบนี้"
            stop sound
            hide depress1ca
            jump question_2_5

label question_2_3:
    menu:
        "ถ้ามีเรื่องไม่สบายใจ อยากจะเล่า เล่าได้นะ เราพร้อมรับฟัง":
            show depress1smilec
            play sound "2tQ3_+1.mp3"
            chin "... อืม ขอบคุณนะ "
            stop sound
            hide depress1smilec
            jump question_2_5
            
        "ถ้ามีปัญหาอะไร ก็บอกกับเราได้นะ":
            show depress1c
            play sound "2tQ3_0.mp3"
            chin "... ไว้โอกาสหน้าละกัน "
            stop sound
            hide depress1c
            jump question_2_6

label question_2_4:
    show npcc
    play sound "2mQ4.mp3"
    npc "เธอดูไม่ค่อยพูดเลยนะ "
    stop sound
    hide npcc
    menu:
        "เธอแค่เหนื่อยใช่ไหม ?":
            show depress1c
            play sound "2tQ4_0.mp3"
            chin "...คงงั้น"
            stop sound
            hide depress1c
            jump question_2_6

        "ถ้าเธอเป็นแบบนี้เพื่อนจะลำบากใจนะ":
            show depress1ca
            play sound "2tQ4_-1.mp3"
            chin "... ขอโทษที่ทำให้ทุกคนลำบากใจ"
            stop sound
            hide depress1ca
            jump question_2_7

label question_2_5:
    show npcc
    play sound "2mQ5.mp3"
    npc " ดูเธอไม่อยากอยู่ที่นี่เลยนะเนี่ย "
    stop sound
    hide npcc
    menu:
        "วันนี้เธออยู่ทำกิจกรรมกับพวกเราก่อนได้ไหม":
            show depress1c
            play sound "2tQ5_0.mp3"
            chin "...อืม ก็ได้"
            stop sound
            hide depress1c
            jump question_2_6

        "ถ้าเธอไม่อยากอยู่ที่นี่ ลองหาที่สงบ ๆ ดีไหม ? ":
            show depress1smilec
            play sound "2tQ5_+1.mp3"
            chin "อือ อาจจะดีกว่านี้ก็ได้ "
            stop sound
            hide depress1smilec
            jump question_2_8

label question_2_6:
    menu:
        "ถ้ามีอะไรไม่โอเคบอกเราได้เสมอนะ":
            show depress1c
            play sound "2tQ1_0.mp3"
            chin "อือ..."
            stop sound
            hide depress1c
            jump question_2_8
            
        "แล้วเราพอช่วยอะไรเธอได้ไหม ? จะอยู่ข้าง ๆ ไม่ต้องกังวลนะ ":
            show depress1smilec
            play sound "2tQ6_+1.mp3"
            chin "อือ ... ขอบคุณนะ เป็นเรื่องที่บ้านน่ะ "
            stop sound
            hide depress1smilec
            jump question_2_8

        "พยายามหน่อยสิ":
            show depress1ca
            play sound "2tQ6_-1.mp3"
            chin "เราจะพยายามนะ "
            stop sound
            hide depress1ca
            jump question_2_7

label question_2_7:
    show npcc
    play sound "2mQ7.mp3"
    npc "เธอคุยกับเราได้นะ พอเห็นเธอเงียบแบบนี้เราก็ทำตัวไม่ถูก"
    stop sound
    hide npcc
    menu:
        "เธอไม่คิดจะปรับตัวให้เข้ากันเพื่อนหน่อยเหรอ":
            show depress1ca
            chin "..."
            hide depress1ca
            jump question_2_9
        
        "ไม่เป็นไรนะ เราค่อย ๆ ทำความรู้จักกันไปเรื่อย ๆ ":
            show depress1c
            play sound "2tQ7_0.mp3"
            chin "ก็จริง ... "
            stop sound
            hide depress1c
            jump question_2_8

label question_2_8:
    scene bg yard at Transform(zoom=3.5) with dissolve
    menu:
        "เราเชื่อว่าเธอจะผ่านไปได้นะ":
            show depress1smilec
            play sound "2tQ8_+1.mp3"
            chin "ขอบคุณนะ"
            stop sound
            hide depress1smilec
            jump good_ending2

        "แค่เธอรู้ว่าเราอยู่ตรงนี้ก็พอ ":
            show depress1c
            play sound "2tQ8_0.mp3"
            chin "อืม ... เข้าใจแล้ว"
            stop sound
            hide depress1c
            jump normal_ending2

label question_2_9:
    show npcc
    play sound "2mQ9.mp3"
    npc "ชินคงยังไม่พร้อมจะพูดอะไร"
    stop sound
    hide npcc
    menu:
        " บางทีเราคงยุ่งกับเธอมากเกินไป":
            show depress1ca
            play sound "2tQ9_-1.mp3"
            chin "เธอให้เราอยู่คนเดียวเถอะ "
            stop sound
            hide depress1ca
            jump bad_ending2
        
        "แค่เธอรู้ว่าเราอยู่ตรงนี้ก็พอ":
            show depress1c
            play sound "2tQ9_0.mp3"
            chin "อืม ... เข้าใจแล้ว"
            stop sound
            hide depress1c
            jump normal_ending2


label good_ending2:
    play sound "2sup_good.mp3"
    show depress1smilec
    "เตชินเริ่มเปิดใจมากขึ้นและมีท่าทีผ่อนคลายขึ้น"
    stop sound
    hide depress1smilec
    window hide
    show sen1
    pause 15.0
    hide sen1
    show sup1
    pause 15.0
    hide sup1
    $ score += 1
    jump university_class

label normal_ending2:
    show depress1c
    play sound "2sup_normal.mp3"
    "เตชินยังคงเก็บตัว แต่ก็ยอมรับการสนับสนุนจากเพื่อน"
    stop sound
    hide depress1c
    window hide
    show sen_1
    pause 15.0
    hide sen_1
    show sup1
    pause 15.0
    hide sup1
    jump university_class

label bad_ending2:
    show depress1ca
    play sound "2sup_bad.mp3"
    "เตชินเลือกที่จะปลีกตัวออกจากกลุ่มและไม่ยอมพูดคุย"
    stop sound
    hide depress1ca
    window hide
    show senn1
    pause 15.0
    hide senn1
    show sup1
    pause 15.0
    hide sup1
    $ score -= 1
    jump university_class

# บทที่ 3
label university_class:
    window auto
    scene bg_class with dissolve
    play sound "3sup1.mp3"
    "ภายในห้องเรียนวิชาศึกษาทั่วไปแสงแดดอ่อน ๆ ส่องผ่านหน้าต่างห้องเรียน นักศึกษาทยอยเข้ามานั่งในห้องเรียน 
    \nเสียงพูดคุยเบา ๆ ลอยไปทั่วห้อง อาจารย์ยืนอยู่หน้าชั้น เตรียมเอกสารสำหรับการเรียนในวันนี้ 
    \nหลังจากสอนเรื่องความสัมพันธ์ในครอบครัวและสังคมเสร็จจึงได้สั่งงานในนักศึกษาทำ "
    stop sound

    scene bg class with dissolve
    play sound "อาจารย์_2_3.mp3"
    aj "วันนี้เราได้เรียนรู้เรื่องความสัมพันธ์ในครอบครัวและสังคมกันไปแล้วนะคะ 
    \nงั้นทุกคนลองเขียนเล่าเกี่ยวกับความสัมพันธ์ในครอบครัวของตัวเอง 
    \nเป็นการส่งงานเพื่อเช็กชื่อ อาจารย์ให้เวลา 30 นาทีส่งเสร็จสามารถกลับได้เลยนะคะ"
    stop sound

    show npcc
    play sound "3mQ1.mp3"
    npc "คิดไม่ออกเหรอชิน"
    stop sound
    hide npcc
    window auto

    menu:
        "เราว่าเรื่องครอบครัวนี่ก็เขียนยากเหมือนกันเนอะ":
            show depress1c
            play sound "3tQ1_0.mp3"
            chin "ใช่ บางเรื่องก็ไม่รู้จะเริ่มจากตรงไหน"
            stop sound
            hide depress1c
        
        "ก็แค่เขียนไปตามโจทย์ อย่าคิดอะไรมาก":
            show depress1c
            play sound "3tQ1_-1.mp3"
            chin "... อือ "
            stop sound
            hide depress1c
            jump question_3_4    
        
        "ลองเขียนเล่าช่วงเวลาที่ทำให้เธอมีความสุขก็ได้":
            show depress1smilec
            play sound "3tQ1_+1.mp3"
            chin "เป็นความคิดที่ดีนะ"
            stop sound
            hide depress1smilec
            jump question_3_2

label question_3_2:
    show npcr
    play sound "3mQ2.mp3"
    npc "พวกเธอเขียนอะไรกันบ้าง ? เรายังไม่รู้จะเริ่มตรงไหนขอดูของเธอได้ไหม"
    stop sound
    show player bl
    b"เราว่าจะเริ่มจากสมาชิกในครอบครัวนะ แล้วก็ความชอบแต่ละคน กิจกรรมที่ชอบทำด้วยกันน่ะ"
    hide npcr
    hide player bl
    menu:
        "เธอยังไม่เริ่มเขียนอีกเหรอ":
            show depress1ca
            play sound "3tQ2_-1.mp3"
            chin "... ยัง "
            stop sound
            hide depress1ca
            jump question_3_4
            
        "เธอเขียนเกี่ยวกับอะไรบ้างอะ ?":
            show depress1c
            play sound "3tQ2_0.mp3"
            chin "ก็คงเป็นเรื่องทั่ว ๆ ไป "
            stop sound
            hide depress1c
            jump question_3_3
            
        "แล้วชินล่ะ จะเขียนถึงอะไรเหรอ พอจะบอกเราได้ไหม ?":
            show depress1c
            play sound "3tQ2_+1.mp3"
            chin "อาจจะเขียนถึงแม่ คือเราสนิทกับแม่น่ะ"
            stop sound
            hide depress1c
            jump question_3_3

label question_3_3:
    play sound "5_min.mp3"
    "เหตุการณ์ผ่านไป 5 นาที"
    stop sound
    show npcl
    play sound "3mQ3.mp3"
    npc "เขียนถึงไหนกันแล้วเหรอ ?"
    stop sound
    show depress1r
    play sound "3tQ3.mp3"
    chin "ตอนนี้ยังนึกไม่ออกว่าจะเขียนอะไรเพิ่มเลยน่ะ"
    stop sound
    hide depress1r
    hide npcl 
    menu:
        "ไม่เป็นไร ค่อย ๆ คิด ไม่ต้องลงรายละเอียดมากก็ได้":
            show depress1c
            play sound "3tQ3_0.mp3"
            chin "อืม..."
            stop sound
            hide depress1c
            jump question_3_6
        
        "ค่อย ๆ เขียนนะ, เราก็เพิ่งเขียนได้นิดเดียวเหมือนกัน":
            show depress1smilec
            play sound "3tQ3_+1.mp3"
            chin "อือ"
            stop sound
            hide depress1smilec
            jump question_3_5

label question_3_4:
    play sound "5_min.mp3"
    "เหตุการณ์ผ่านไป 5 นาที"
    stop sound
    show npcl
    play sound "3mQ4.mp3"
    npc "เขียนถึงไหนกันแล้วเหรอ ?"
    stop sound
    show depress1r
    play sound "3tQ4.mp3"
    chin "พึ่งเขียนได้นิดหน่อยน่ะ"
    stop sound
    hide depress1r
    hide npcl
    menu:        
        "รีบ ๆ เขียนไปเหอะ อย่าซีเรียสแค่เขียนส่งเช็กชื่อเอง ":
            show depress1ca
            play sound "3tQ4_-1.mp3"
            chin "อืม..."
            stop sound
            hide depress1ca
            jump question_3_7

        "ไม่เป็นไร ค่อย ๆ คิด เขียนแบบทั่ว ๆ ไปก็ได้ ":
            show depress1smilec
            play sound "3tQ4_0.mp3"
            chin "อืม ... เรื่องทั่วไปน่าจะเขียนง่ายกว่า"
            stop sound
            hide depress1smilec
            jump question_3_6

label question_3_5:
    play sound "10_min.mp3"
    "เหตุการณ์ผ่านไป 10 นาที "
    stop sound
    show npcc
    play sound "3mQ5.mp3"
    npc "เย่ ! จะเสร็จแล้ว พวกเธอเขียนใกล้เสร็จกันรึยัง ?"
    stop sound
    show player br
    b "เราเขียนใกล้เสร็จแล้วเหมือนกัน"
    hide player br
    hide npcc
    menu:
        "แล้วเธอเขียนเสร็จรึยังเหรอชิน เขียนแบบทั่ว ๆ ไปก็ได้":
            show depress1c
            play sound "3tQ5_0.mp3"
            chin "เสร็จแล้ว เขียนไปนิดเดียว "
            stop sound
            hide depress1c
            jump question_3_9
            
        "แล้วชินล่ะ ? ยังมีเวลาเหลือนะ พึ่งผ่านมา 10 นาทีเอง":
            show depress1smilec
            play sound "3tQ5_+1.mp3"
            chin "อือ…ใกล้เสร็จแล้ว แต่เราเขียนได้แค่นิดเดียวเอง"
            stop sound
            hide depress1smilec
            jump question_3_8

label question_3_6:
    play sound "10_min.mp3"
    "เหตุการณ์ผ่านไป 10 นาที "
    stop sound
    show npcc
    play sound "3mQ6.mp3"
    npc "ใกล้หมดเวลาแล้วนะ เขียนใกล้เสร็จกันรึยัง ?"
    stop sound
    show player br
    b "เราเขียนใกล้เสร็จแล้ว"
    hide player br
    hide npcc
    menu:
        "ชินเธอทำใกล้เสร็จรึยัง ถ้ายังไม่ต้องรีบนะยังพอมีเวลาอยู่":
            show depress1smilec
            play sound "3tQ6_+1.mp3"
            chin "อือ…ใกล้เสร็จแล้ว แต่เราเขียนได้แค่นิดเดียวเอง"
            stop sound
            hide depress1smilec
            jump question_3_8

        "ใกล้หมดเวลาแล้วนะ เราว่าถ้ายังไม่เสร็จเขียนอะไรได้ก็รีบส่ง ๆ ไปก่อนเหอะ":
            show depress1ca
            play sound "3tQ6_-1.mp3"
            chin "อือ เขียนเสร็จแล้ว "
            stop sound
            hide depress1ca
            jump question_3_10
            
        "แล้วเธอเขียนใกล้เสร็จรึยังเหรอชิน":
            show depress1c
            play sound "3tQ6_0.mp3"
            chin "เสร็จแล้ว เราเขียนได้นิดเดียว"
            stop sound
            hide depress1c
            jump question_3_9
    
label question_3_7:
    play sound "10_min.mp3"
    "เหตุการณ์ผ่านไป 10 นาที "
    stop sound
    show npcc
    play sound "3mQ7.mp3"
    npc "ใกล้หมดเวลาแล้วนะ เขียนใกล้เสร็จกันรึยัง ?"
    stop sound
    show player br
    b "เราเขียนใกล้เสร็จแล้ว"
    hide player br
    hide npcc
    menu:
        "จะหมดเวลาแล้วนะ ถ้ายังไม่เสร็จเขียนอะไรได้ก็รีบส่ง ๆ ไปก่อนเหอะ":
            show depress1ca
            play sound "3tQ7_-1.mp3"
            chin "อือ เขียนเสร็จแล้ว "
            stop sound
            hide depress1ca
            jump question_3_10
            
        "แล้วเธอเขียนใกล้เสร็จรึยังเหรอชิน เขียนแบบทั่ว ๆ ไปก็ได้":
            show depress1c
            play sound "3tQ7_0.mp3"
            chin "เสร็จแล้ว เราเขียนได้นิดเดียว"
            stop sound
            hide depress1c
            jump question_3_9

label question_3_8:
    show npcc
    play sound "3mQ8.mp3"
    npc "เฮ้อออ เขียนเรื่องครอบครัวนี่มันไม่ง่ายเลยนะเนี้ย"
    stop sound
    show player br
    b "ใช่ไหม ทั้งที่เป็นเรื่องใกล้ตัว แต่พอให้เขียนก็ไม่รู้จะเขียนอะไรดี"
    show depress1
    play  sound "3tQ8.mp3"
    chin "สำหรับเรา เราว่าเรื่องนี้ยากที่สุด"
    stop sound
    hide depress1
    hide player br
    hide npcc
    menu:
        "เธอโอเคขึ้นรึยัง เมื่อกี้เราเห็นเธอดูเครียด ๆ ":
            show depress1c
            play sound "3tQ8_0.mp3"
            chin "เราไม่ได้เป็นอะไร เราไม่สนิทกับพ่อขนาดนั้นเลยไม่รู้จะเขียนอะไร"
            stop sound
            hide depress1c
            jump normal_ending3
            
        "ชินเธอเป็นไงบ้างเราเห็นเธอทำหน้าเครียดตอนเขียนน่ะ มีอะไรลองบอกเราได้นะ ":
            show depress1smilec
            play sound "3tQ8_+1.mp3"
            chin "ดีขึ้นแล้ว คือ ... พ่อชอบกดดันเราในหลาย ๆ เรื่องน่ะ
            \nแล้วก็ไม่สนิทกับพ่อด้วย เลยไม่รู้จะเขียนอะไร "
            stop sound
            hide depress1smilec
            jump good_ending3

label question_3_9:
    menu:
        "เมื่อกี้ชินทำหน้าเครียดจัง ไม่ต้องไปคิดมากหรอกแค่งานเช็กชื่อเอง":
            show depress1ca
            play sound "3tQ9_-1.mp3"
            chin "อ่า ... งั้นเหรอ"
            stop sound
            hide depress1ca
            jump bad_ending3
            
        "เธอโอเคขึ้นรึยัง เมื่อกี้เราเห็นเธอดูเครียด ๆ ":
            show depress1c
            play sound "3tQ9_0.mp3"
            chin "เราไม่ได้เป็นอะไร เราไม่สนิทกับพ่อขนาดนั้นเลยไม่รู้จะเขียนอะไร"
            stop sound
            hide depress1c
            jump normal_ending3
            
        "ชินเธอเป็นไงบ้างเราเห็นเธอทำหน้าเครียดตอนเขียนน่ะ มีอะไรลองบอกเราได้นะ ":
            show depress1smilec
            play sound "3tQ9_+1.mp3"
            chin "ดีขึ้นแล้ว คือ ... พ่อชอบกดดันเราในหลาย ๆ เรื่องน่ะ
            \nแล้วก็ไม่สนิทกับพ่อด้วย เลยไม่รู้จะเขียนอะไร "
            stop sound
            hide depress1smilec
            jump good_ending3

label question_3_10:
    show npcc
    play sound "3mQ10.mp3"
    npc "เฮ้อออ เขียนเรื่องครอบครัวนี่มันไม่ง่ายเลยนะเนี้ย"
    stop sound
    show player br
    b "ก็จริงนะ พอคิดไม่ออกก็เขียนยากเลย"
    hide player br
    hide npcc
    menu:
        "เครียดทำไม แค่งานเช็กชื่อเอง ":
            show depress1ca
            play sound "3tQ10_-1.mp3"
            chin "อ่า ... งั้นเหรอ"
            stop sound
            hide depress1ca
            jump bad_ending3

        "เธอโอเคขึ้นรึยัง เมื่อกี้เราเห็นเธอดูเครียด ๆ ":
            show depress1c
            play sound "3tQ10_0.mp3"
            chin "เราไม่ได้เป็นอะไร เราไม่สนิทกับพ่อขนาดนั้นเลยไม่รู้จะเขียนอะไร"
            stop sound
            hide depress1c
            jump normal_ending3

label good_ending3:
        play sound "3sup_good.mp3"
        "เตชินเริ่มกล้าพูดถึงความรู้สึกของตัวเองมากขึ้น แม้จะยังไม่ทั้งหมด"
        stop sound
        window hide
        show good3
        pause 15.0
        hide good3
        show sup2
        pause 15.0
        $ score += 1
        jump cafe

label normal_ending3:
        play sound "3sup_normal.mp3"
        "เตชินยังไม่พร้อมเปิดใจ แต่ก็ไม่ปฏิเสธการอยู่เคียงข้างของเพื่อน"
        stop sound
        window hide
        show normal3
        pause 15.0
        hide normal3
        show sup2
        pause 15.0
        jump cafe

label bad_ending3:
        play sound "3sup_bad.mp3"
        "เตชินเลือกเก็บความรู้สึกไว้กับตัวเอง และหลีกเลี่ยงการพูดถึงครอบครัว"
        stop sound
        window hide
        show bad3
        pause 15.0
        hide bad3
        show sup2
        pause 15.0
        $ score -= 1
        jump cafe

# บทที่ 4
label cafe:
    window auto
    scene cafe_out with dissolve
    play sound "4sup1.mp3"     # เสีบงบรรยาย
    "ที่ร้าน café ในตอนบ่าย คุณกับเมย์เดินเข้ามาสั่งเครื่องดื่ม
    \nแล้วพบเตชินนั่งอยู่ในมุมร้านกับหนังสือกองโต สีหน้าดูเคร่งเครียดผิดปกติ คุณจึงเดินเข้าไปทัก "
    stop sound
    scene chincafe with dissolve
    show player bl
    b "ไงชิน เปลี่ยนที่อ่านหนังสือเหรอ ? "
    scene cafe with dissolve
    show chinr
    play sound "4t1.mp3"
    chin "สวัสดี ก็ใช่ ... อ่านอยู่ในห้องแล้วไม่มีสมาธิ"
    stop sound
    show may
    play sound "4m1P.mp3"
    npc "เรากับปุณเพิ่งสั่งเครื่องดื่มเสร็จ ขอนั่งด้วยได้ไหม"
    stop sound
    play sound "4t2.mp3"
    chin "อืม นั่งเลยตามสบาย"
    stop sound
    hide may
    hide player bl
    hide chinr
    show npcc
    play sound "4mQ1.mp3"
    npc "ทำไมเธออ่านเยอะจัง ?"
    stop sound
    hide npcc

    menu:
        "ทำไมต้องเครียดขนาดนั้น ? อ่านอะไร":
            show chinca
            play sound "4tQ1_-1.mp3"
            chin "พรุ่งนี้มีสอบซ่อม"
            stop sound
            hide chinca
            jump question_4_4

        "มีสอบอะไรเหรอ ? ดูจริงจังมากเลย":
            show chinc
            play sound "4tQ1_+1.mp3"
            chin "พอดีสอบแล็บไม่ผ่านน่ะ เลยต้องสอบซ่อมพรุ่งนี้"
            stop sound
            hide chinc
            jump question_4_2

        "อ่านเยอะขนาดนี้มีสอบอะไรเหรอ ?":
            show chinc_n
            play sound "4tQ1_0.mp3"
            chin "อืม สอบซ่อมแล็บอะ"
            stop sound
            hide chinc_n
            jump question_4_3

label question_4_2:
    show may
    play sound "4mQ2.mp3"
    npc "พักกินของหวานกันก่อนดีไหม ?"
    stop sound
    show player bl
    b "ช่วงเครียด ๆ นี่แหละต้องกินของหวาน"
    show chinr
    play sound "4tQ2.mp3"
    chin "ก็ดีเหมือนกันนะ แต่เราขอนั่งอ่านอีกแปปหนึ่งนะ"
    stop sound
    hide player bl
    hide chinr
    hide may
    menu:
        "อย่างน้อยยังมีโอกาสสอบซ่อมนะ เราเชื่อว่าเธอทำได้":
            show chinc_n
            play sound "4tQ2_0.mp3"
            chin "อือ ... หวังว่าคราวนี้จะผ่านไปได้ล่ะนะ"
            stop sound
            hide chinc_n
            jump question_4_5

        "เราอาจช่วยเรื่องสอบไม่ได้ แต่เดี๋ยวเรานั่งอยู่เป็นเพื่อนตรงนี้นะ":
            show chinc
            play sound "7tQ1_+1.mp3"
            chin "... อืม ขอบใจนะ "
            stop sound
            hide chinc
            jump good_ending4

label question_4_3:
    show may
    play sound "4mQ3.mp3"
    npc "แล้วสอบที่ผ่านมา ก็สอบแล็บเหมือนกันเหรอ ?"
    stop sound
    show chinc
    play sound "4tQ3.mp3"
    chin "ใช่"
    stop sound
    hide may
    hide chinc
    menu:
        "ก็ลองตั้งใจดู สู้ ๆ นะ":
            show chinca
            play sound "4tQ3_-1.mp3"
            chin "... ขอบใจ"
            stop sound
            hide chinca
            jump question_4_6
            
        " ลองทำสรุปไหม เราว่าอาจจะช่วยได้นะ":
            show chinc
            play sound "4tQ3_+1.mp3"
            chin "ขอบใจนะ เดี๋ยวลองดู เผื่อช่วยจัดการความคิดได้ 
                \nตอนนี้เรากังวลน่ะเลยจัดการความคิดไม่ได้ "
            stop sound
            hide chinc
            jump question_4_5

        "ก็ยากจริง ๆ นั่นแหละ":
            show chinc_n
            play sound "4tQ3_0.mp3"
            chin "ใช่ ... แค่เห็นก็เหนื่อยแล้ว "
            stop sound
            hide chinc_n
            jump normal_ending4

label question_4_4:
    menu:
        "งั้นก็พยายามหน่อยนะ เห็นทำหน้าเครียดแล้วเราเครียดตาม":
            show chinca
            play sound "4tQ4_-1.mp3"
            chin "...ขอโทษนะ ถ้าทำให้รู้สึกลำบากใจ "
            stop sound
            hide chinca
            jump bad_ending4
            
        "ไม่ต้องฝืนตัวเองนะ":
            show chinc_n
            play sound "4tQ4_0.mp3"
            chin "ขอบใจนะ ... "
            stop sound
            hide chinc_n
            jump question_4_6

label question_4_5:
    menu:
        "รอบหน้าก็อย่าพลาดอีกแล้วกันนะ":
            show chinca
            play sound "4tQ5_-1.mp3"
            chin "... เรารู้อยู่แล้ว ... ไม่ต้องตอกย้ำ "
            stop sound
            hide chinca
            jump bad_ending4
            
        "เธอไม่ได้อยู่ตัวคนเดียวนะ ยังมีพวกเราอยู่":
            show chinc
            play sound "4tQ5_+1.mp3"
            chin "ดีใจที่มีพวกเธออยู่ตรงนี้ "
            stop sound
            hide chinc
            jump good_ending4
            
        "ค่อย ๆ อ่านนะ ยังมีเวลาอยู่":
            show chinc_n
            play sound "4tQ5_0.mp3"
            chin "อือ ... จะพยายามให้ดีที่สุดเหมือนกัน "
            stop sound
            hide chinc_n
            jump normal_ending4

label question_4_6:
    show npcc
    play sound "4mQ6.mp3"
    npc "ถ้าไม่ไหวก็บอกได้นะ"
    stop sound
    hide npcc
    menu:            
        "เรื่องแค่นี้ยังจัดการไม่ได้เลย ?":
            show chinca
            play sound "4tQ6_-1.mp3"
            chin "เราขออยู่เงียบ ๆ สักพักนะ ... "
            stop sound
            hide chinca
            jump bad_ending4

        "เราเป็นกำลังใจให้":
            show chinc_n
            play sound "4tQ6_0.mp3"
            chin "อือ ... ขอบใจนะ "
            stop sound
            hide chinc_n
            jump normal_ending4

label good_ending4:
    play sound "4sup_good.mp3"
    "เตชินยอมรับว่าตัวเองกำลังเหนื่อย และเปิดใจรับความห่วงใยจากคนรอบข้าง"
    stop sound
    window hide
    show good4
    pause 15.0
    hide good4
    show sup3
    pause 15.0
    hide sup3
    $ score += 1
    jump university_class2

label normal_ending4:
    play sound "4sup_normal.mp3"
    "เตชินยังคงฝืนตัวเอง แต่ก็รู้ว่ามีคนคอยเป็นห่วงเขาอยู่"
    stop  sound
    window hide
    show normal4
    pause 15.0
    hide normal4
    show sup3
    pause 15.0
    hide sup3
    jump university_class2

label bad_ending4:
    play sound "4sup_bad.mp3"
    "เตชินปิดกั้นความรู้สึกของตัวเอง และเลือกเผชิญทุกอย่างเพียงลำพัง"
    stop sound
    window hide
    show bad4
    pause 15.0
    hide bad4
    show sup3
    pause 15.0
    hide sup3
    $ score -= 1
    jump university_class2

# บทที่ 5
label university_class2:
    window auto
    scene bg_class with dissolve
    play sound "5sup1.mp3"
    "ในห้องเรียนวิชาศึกษาทั่วไป – กลุ่มของเตชิน 5 คน รวมตัวกันเพื่อช่วยกันคิดบท
    \nสำหรับแสดงบทบาทสมมุติหน้าชั้นเรียนซึ่งกลุ่มของเตชินจับฉลากได้หัวข้อความสัมพันธ์ในครอบครัว"
    stop sound
    show may
    play sound "5m1.mp3"
    npc "เราเอาบท แม่ แล้วกันนะ"
    stop sound
    show player br
    b "งั้นเราขอบท ลูกนะ ชินเล่นบทพ่อได้ไหม "
    play sound "5mQ1.mp3"
    npc "เธอโอเคไหมกับบทนี้ ? เราปรับคำพูดได้นะ"
    stop sound
    hide may
    hide player br
    menu:
        "ก็แค่แสดงบทบาทสมมุตินะ ไม่เห็นต้องคิดมากเลยก็ได้มั้ง":
            show depress1c
            play sound "5tQ1_-1.mp3"
            chin "ถ้าทำได้แบบนั้นก็ดีสิ"
            stop sound
            show npcr
            play sound "5m2.mp3"
            npc "จริง ๆ เราก็เคยเจอบทที่สะกิดความรู้สึกเหมือนกัน ... มันไม่ง่ายเลยนะ"
            stop sound
            show player bl
            b "ก็ใช่ ... เรื่องครอบครัวมันเป็นเรื่องอ่อนไหวเนอะ "
            hide depress1c
            hide npcr
            hide player bl
            jump question_5_4
            
        "หรือชินอยากสลับบทกับเราก็ได้นะ ?":
            show depress1c
            play sound "5tQ1_0.mp3"
            chin "ไม่ต้องหรอก เราจะลองดูก่อน "
            stop sound
            show npcr
            play sound "5m2.mp3"
            npc "จริง ๆ เราก็เคยเจอบทที่สะกิดความรู้สึกเหมือนกัน ... มันไม่ง่ายเลยนะ"
            stop sound 
            show player bl
            b "ก็ใช่ ... เรื่องครอบครัวมันเป็นเรื่องอ่อนไหวเนอะ "
            hide depress1c
            hide npcr
            hide player bl
            jump question_5_3

        "ไม่ต้องฝืนนะ แต่เราอยากให้ชินแสดงบทในแบบที่ชินสบายใจมากกว่านะ":
            show depress1c
            play sound "5tQ1_+1.mp3"
            chin "อืม ... ขอบใจนะที่เข้าใจ"
            stop sound
            show npcr
            play sound "5m2.mp3"
            npc "จริง ๆ เราก็เคยเจอบทที่สะกิดความรู้สึกเหมือนกัน ... มันไม่ง่ายเลยนะ"
            stop sound
            show player bl
            b "ก็ใช่ ... เรื่องครอบครัวมันเป็นเรื่องอ่อนไหวเนอะ "
            hide depress1c
            hide npcr
            hide player bl
            jump question_5_2
            
        

label question_5_2:
    menu:            
        "เรามาซ้อมบทกัน":
            show depress1c
            play sound "5tQ3_-1.mp3"
            chin "อืม ... ก็ได้ "
            stop sound
            hide depress1c
            jump question_5_5

        "งั้นเดี๋ยวเราซ้อมบทกัน เธอพร้อมตอนไหนก็ได้ เราเอาตามที่ชินสะดวกเลย":
            show depress1smilec
            play sound "5tQ2_+1.mp3"
            chin "งั้น ... เดี๋ยวซ้อมทีละฉากแล้ว"
            stop sound
            hide depress1smilec
            jump good_ending5

label question_5_3:
    menu:
        "งั้นซ้อมเท่าที่ได้ก่อนละกัน":
            show depress1c
            play sound "5tQ3_0.mp3"
            chin "อืม ... เราจะพยายาม"
            stop sound
            hide depress1c
            jump normal_ending5
            
        "งั้นเดี๋ยวเราซ้อมบทกัน เธอพร้อมตอนไหนก็ได้ เราเอาตามที่ชินสะดวกเลย":
            show depress1smilec
            play sound "5tQ3_+1.mp3"
            chin "งั้น ... เดี๋ยวซ้อมทีละฉากแล้ว"
            stop sound
            hide depress1smilec
            jump question_5_5

        "พร้อมยัง รีบซ้อมบทเถอะ เพื่อนจะได้ไปทำอย่างอื่น":
            show depress1ca
            play sound "5tQ3_-1.mp3"
            chin "... อือ ก็ได้ "
            stop sound
            hide depress1ca
            jump question_5_6

label question_5_4:
    menu:
        "พร้อมยัง รีบซ้อมบทเถอะ เพื่อนจะได้ไปทำอย่างอื่น":
            show depress1c
            play sound "5tQ4_0.mp3"
            chin " ... อือ ก็ได้ "
            stop sound
            hide depress1c
            jump question_5_6

        "ก็แค่ซ้อมบทปะ จะจริงจังทำไม ?":
            show depress1ca
            chin "..."
            hide depress1ca
            jump bad_ending5

label question_5_5:
    show player br
    b "ชิน ถ้ามีเรื่องไม่สบายใจเธอเล่าให้เราฟังได้นะ ?"
    show depress1
    play sound "5tQ5.mp3"
    chin "เราไม่เข้าใจบทพ่อน่ะ มันทำให้เรานึกถึงพ่อเรา "
    stop sound
    hide player br
    hide depress1
    menu:
        "งั้นเดี๋ยวปรับบทพ่อให้พูดน้อย ๆ ละกัน":
            show depress1c
            play sound "5tQ5_0.mp3"
            chin "แบบนั้นก็ได้"
            stop sound
            hide depress1c
            jump normal_ending5
            
        "เธอสามารถพูดออกมาได้นะ เผื่อเราจะช่วยอะไรได้":
            show depress1c
            play sound "5tQ5_+1.mp3"
            chin "คือสำหรับเราพ่อคือคนที่คอยบงการชีวิต โดยที่ไม่ถามความรู้สึกของเราเลย "
            stop sound
            hide depress1c
            jump good_ending5
            
label  question_5_6:
    menu:
        "อย่าคิดมากก็แค่แสดงบทบาทสมมุติเอง พูดไปตามบทนั่นแหละ":
            show depress1ca
            chin "..."
            hide depress1ca
            jump bad_ending5
            
        "งั้นเดี๋ยวปรับบทพ่อให้พูดน้อย ๆ ละกัน ":
            show depress1c
            play sound "5tQ6_0.mp3"
            chin "แบบนั้นก็ได้  "
            stop sound
            hide depress1c
            jump normal_ending5
    
label good_ending5:
    play sound "5sup_good.mp3"
    "เตชินเริ่มรู้ว่าเขาไม่จำเป็นต้องแบกรับทุกอย่างไว้คนเดียว"
    stop sound
    window hide
    show good5
    pause 15.0
    hide good5
    show sup4
    pause 15.0
    hide sup4
    $ score += 1
    jump university_class3

label normal_ending5:
    play sound "5sup_normal.mp3"
    "เตชินพยายามทำหน้าที่ของตัวเอง แม้จะยังรู้สึกกดดันอยู่"
    stop  sound
    window hide
    show normal5
    pause 15.0
    hide normal5
    show sup4
    pause 15.0
    hide sup4
    jump university_class3

label bad_ending5:
    play sound "5sup_bad.mp3"
    "เตชินโทษตัวเองที่ทำไม่ได้ตามที่คาดหวัง และเริ่มถอยห่างจากกลุ่ม"
    stop sound
    window hide
    show bad5
    pause 15.0
    hide bad5
    show sup4
    pause 15.0
    hide sup4
    $ score -= 1
    jump university_class3

# บทที่ 6
label university_class3:
    window auto
    scene bg class with dissolve
    play sound "6sup1.mp3"
    "เมื่อเริ่มคลาสนักศึกษาทุกคนนั่งอยู่ในห้องเรียน หลังจากอาจารย์สอนเสร็จ
    \nได้ให้เขียนถึงความสัมพันธ์ที่เปลี่ยนไปในช่วงหนึ่งของชีวิต "
    stop sound
    play sound "อาจารย์_2_6.mp3"
    aj "ให้นักเรียนทุกคนเขียนเรื่องสั้น เกี่ยวกับความสัมพันธ์กับบุคคลที่เปลี่ยนไปในชีวิต
    \nไม่ว่าจะเป็นเรื่องที่ดีหรือไม่ดี ให้ส่งท้ายชั่วโมงนะคะ"
    stop sound
    show npcr
    play sound "6m1.mp3"
    npc "อาจารย์ให้โจทย์อะไรมาเนี้ย "
    stop sound
    show player bl
    b "แค่คิดว่าจะเล่าเรื่องไหนก็ลังเลแล้ว เพราะมีหลายเรื่อง"
    show depress1c
    play sound "6t1.mp3"
    chin "บางเรื่องพอมันเปลี่ยนไปแล้ว ... มันก็กลับมาเหมือนเดิมไม่ได้อีกเลย"
    stop sound
    hide npcr
    hide player bl
    hide depress1c
    menu:
        "ความสัมพันธ์ก็เปลี่ยนไปตามเวลาเองแหละเนอะ ":
            show depress1c
            play sound "6tQ1_0.mp3"
            chin "ใช่ บางทีก็ค่อย ๆ ห่างกันไป "
            stop sound
            show npcr
            play sound "6m2.mp3"
            npc "เราว่าความรู้สึกตอนความสัมพันธ์เปลี่ยนไป เหมือนทำของสำคัญหล่นหายเลยนะ"
            stop sound
            play sound "6t2.mp3"
            chin "อืม ... บางครั้งเราก็ไม่ทันรู้ว่ามันหายไปตั้งแต่เมื่อไหร่ด้วยซ้ำ"
            stop sound
            hide npcr
            hide depress1c
            jump question_6_3

        "เรื่องแบบนี้ก็เจอทุกคนแหละ เรื่องปกติ ":
            show depress1ca
            chin "..."
            show npcr
            play sound "6m2.mp3"
            npc "เราว่าความรู้สึกตอนความสัมพันธ์เปลี่ยนไป เหมือนทำของสำคัญหล่นหายเลยนะ"
            stop sound
            hide depress1ca
            show depress1c
            play sound "6t2.mp3"
            chin "อืม ... บางครั้งเราก็ไม่ทันรู้ว่ามันหายไปตั้งแต่เมื่อไหร่ด้วยซ้ำ"
            stop sound
            hide npcr
            hide depress1c
            jump question_6_4
            
        "หมายถึงเรื่องครอบครัวเหรอ ? ":
            show depress1c
            play sound "6tQ1_+1.mp3"
            chin "... ใช่ เรื่องทางบ้านแหละ แต่ก็ไม่ค่อยได้พูดถึง"
            stop sound
            show npcr
            play sound "6m2.mp3"
            npc "เราว่าความรู้สึกตอนความสัมพันธ์เปลี่ยนไป เหมือนทำของสำคัญหล่นหายเลยนะ"
            stop sound
            play sound "6t2.mp3"
            chin "อืม ... บางครั้งเราก็ไม่ทันรู้ว่ามันหายไปตั้งแต่เมื่อไหร่ด้วยซ้ำ"
            stop sound
            hide npcr
            hide depress1c
            jump question_6_2

label question_6_2:
    menu:
        "งั้นก็ช่างเถอะ เรื่องมันผ่านไปแล้ว":
            show depress1c
            play sound "6tQ2_0.mp3"
            chin "อือ เรื่องผ่านไปแล้ว"
            stop sound
            hide depress1c
            jump question_6_5
            
        "เธอเล่าให้เราฟังได้นะ ? เราพร้อมรับฟังอยู่เสมอนะ":
            show depress1c
            play sound "6tQ2_+1.mp3"
            chin "ขอบใจนะ ช่วงที่แม่เราป่วยน่ะ เราอยากอยู่ดูแลแม่ 
            \nแต่เราไม่สามารถติดต่อแม่ได้เลย"
            stop sound
            hide depress1c
            jump good_ending6

label question_6_3:
    show player br
    b "แล้วเธอรู้สึกยังไงเหรอตอนนั้น ?"
    show depress1
    play sound "6t3.mp3"
    chin "ตอนแรกก็รู้สึกแปลก ๆ ความรู้สึกเหมือนมีอะไรหายไป"
    stop sound
    hide depress1
    hide player br
    menu:
        "แต่ถ้ามันหายไปง่ายขนาดนั้นก็คงไม่สำคัญตั้งแต่แรกแล้วไหม ?": #-1
            show depress1c
            play sound "2tQ4_0.mp3"
            chin "...คงงั้น"
            stop sound
            show npcl
            play sound "6m3.mp3"
            npc "บางคนอยู่ดี ๆ หายไป"
            stop sound
            show player br
            b "ก็จริง ... "
            hide player br
            hide npcl
            hide depress1c
            jump question_6_6
            
        "เราเข้าใจนะ บางความสัมพันธ์หายไปเฉย ๆ ก็ยังฝังใจ": #+1
            show depress1c
            play sound "6tQ3_+1.mp3"
            chin "มันเหมือน ... เราไม่มีโอกาสถามว่า ‘ทำไม’ "
            stop sound
            show npcl
            play sound "6m3.mp3"
            npc "บางคนอยู่ดี ๆ หายไป"
            stop sound
            show player br
            b "ก็จริง ... "
            hide player br
            hide npcl
            hide depress1c
            jump question_6_5

        "บางครั้งมันก็เป็นธรรมชาติของการโตขึ้นเนอะ": #0
            show depress1c
            play sound "6tQ3_0.mp3"
            chin "อืม ... ใช่ แต่บางครั้งก็ยังรู้สึกแปลก ๆ อยู่ดี"
            stop sound
            show npcl
            play sound "6m3.mp3"
            npc "บางคนอยู่ดี ๆ หายไป"
            stop sound
            show player br
            b "ก็จริง ... "
            hide player br
            hide npcl
            hide depress1c
            jump normal_ending6

label question_6_4:
    menu :
        "ไม่อยากเล่าก็ไม่ต้องเล่า เราแค่ถามเฉย ๆ":
            show depress1c
            play sound "6tQ4_-1.mp3"
            chin "... ขอโทษนะ งั้นเราขอตัวไปหาที่เขียนเงียบ ๆ ดีกว่า"
            stop sound
            jump bad_ending6
            
        "เป็นเพื่อนเหรอ ? หรือครอบครัว ?":
            show depress1c
            play sound "6tQ4_0.mp3"
            chin "คนในครอบครัวน่ะ"
            stop sound
            jump question_6_6

label question_6_5:
    show player bc
    b "เธอได้เรียนรู้อะไรจากเรื่องที่มันเปลี่ยนแปลงไปไหม ?"
    b "เราว่า ... "
    hide player bc
    menu :
        "ถึงมันเปลี่ยนไป แต่เราก็เลือกได้นะว่าจะจดจำมันยังไง ":
            show depress1c
            play sound "6tQ5_+1.mp3"
            chin "เราไม่เคยคิดแบบนั้นมาก่อน"
            stop sound
            jump good_ending6
        
        "มันอาจจะไม่หายเจ็บ แต่มันก็ทำให้เราเข้มแข็งขึ้น":
            show depress1c
            play sound "6tQ5_0.mp3"
            chin "ใช่ ... มันทำให้เราเข้มแข็งขึ้น แต่สุดท้ายก็เหลือแค่เราอยู่ดี "
            stop sound
            jump normal_ending6

label question_6_6:
    show player bl
    b "ถ้าได้คุยกับคนนั้นอีกครั้ง เธออยากพูดอะไร ?"
    hide player bl
    menu :
        "แต่มันอาจไม่มีประโยชน์อะไรแล้วก็ได้มั้ง":
            show depress1c
            play sound "6tQ6_-1.mp3"
            chin " นั่นแหละ ... "
            stop sound
            jump bad_ending6
            
        "เราว่าถ้าเขาฟังสิ่งที่อยู่ในใจเธอ เขาจะเข้าใจเธอก็ได้":
            show depress1c
            play sound "6tQ6_0.mp3"
            chin "หวังว่าอย่างนั้นนะ"
            stop sound
            jump normal_ending6

label good_ending6: 
    hide depress1c
    play sound "6sup_good.mp3"
    "เตชินกล้ายอมรับความเจ็บปวดของตัวเอง และเริ่มมองความสัมพันธ์ในมุมใหม่"
    stop sound
    window hide
    show good6
    pause 15.0
    hide good6
    show sup5
    pause 15.0
    hide sup5
    $ score += 1
    jump cut_scene2

label normal_ending6:
    hide depress1c
    play sound "6sup_normal.mp3"
    "เตชินรับรู้ว่าปัญหาไม่ได้เกิดจากเขาเพียงคนเดียว แต่ยังไม่กล้าเผชิญหน้า"
    stop sound
    window hide
    show normal6
    pause 15.0
    hide normal6
    show sup5
    pause 15.0
    hide sup5
    jump cut_scene2

label bad_ending6:
    hide depress1c
    play sound "6sub_bad.mp3"
    "เตชินรู้สึกผิดกับทุกอย่าง และเลือกเก็บความเจ็บปวดไว้ภายในใจ"
    stop sound
    window hide
    show bad6
    pause 15.0
    hide bad6
    show sup5
    pause 15.0
    $ score -= 1
    hide sup5
    jump cut_scene2

# cut scene 2
label cut_scene2:
    window auto
    scene cs2 with dissolve
    show may
    play sound "cs2m1.mp3"
    npc "โจทย์วันนี้ทำให้นึกย้อนถึงเมื่อก่อนเลยอะ"
    stop sound
    show player_b
    b "นั่นสิ"
    show chinr
    play sound "cs2t_1.mp3"
    chin "บางเรื่อง ... แค่นึกถึงก็รู้สึกไม่ดีแล้ว โดยเฉพาะกับพ่อ "
    stop sound
    b "ชินเคย ... ลองคุยกับพ่อจริง ๆ บ้างไหม ? 
    \nไม่ใช่เรื่องสอบกับเรื่องเรียนนะ แต่ความรู้สึกของชินอะ"
    play sound "cs2t_2.mp3"
    chin "... พูดไปเขาก็คงไม่ฟังหรอก"
    stop sound
    play sound "cs2m2.mp3"
    npc "พ่อของชินอาจไม่ได้เข้าใจทันที แต่ถ้าเธอไม่เริ่มพูด พ่อของเธอก็ไม่มีทางรู้หรอก
    \nเราไม่ได้บอกว่าชินต้องพูดตอนนี้ ... แต่ลองคิดดู ถ้าได้พูดสิ่งเก็บไว้
    \nบางทีเธออาจจะได้รู้ความคิดของพ่อก็ได้นะ"
    stop sound
    play sound "cs2t_3.mp3"
    chin "... เรากลัวว่าถ้าพูดไป มันจะยิ่งแย่กว่าเดิม"
    stop sound
    play sound "cs2m3.mp3"
    npc "พอบอกได้ไหมว่าแย่กว่าเดิมยังไง"
    stop sound
    play sound "cs2t_4.mp3"
    chin "เมื่อก่อนเราเคยบอกพ่อนะ ว่าอยากเรียนโบราณคดีต่อ…ถึงพ่อจะไม่พูดอะไร
    \nแต่สุดท้าย ก็ให้แม่มาบอกให้เราลาออกอยู่ดี พ่อไม่เคยถามเลยว่าเราต้องการอะไร"
    stop sound
    b "ถ้าเป็นแบบนั้น ... อย่างน้อยเธอก็ได้พยายามแล้ว บางทีการเปิดใจ 
    \nอาจไม่ใช่เพื่อให้พ่อเข้าใจ แต่อาจเป็นการให้เราเข้าใจตัวเองก่อนก็ได้นะ"
    play sound "cs2t_5.mp3"
    chin "…จะลองคิดดูละกัน ขอบใจนะ ทั้งสองคนเลย"
    stop sound
    hide may
    hide chinr
    hide player_b
    window hide
    show cs_2
    pause 9.0
    hide cs_2
    jump cut_scene3

# cut scene 3
label cut_scene3:
    window auto
    scene living with dissolve
    play sound "cs3sup.mp3"
    "เตชินกลับไปบ้านแล้วตัดสินใจที่จะคุยกับพ่อ เขาจึงไปหาพ่อห้องรับแขก มีเสียงโทรทัศน์แผ่ว ๆ มาจากในห้อง
    \nพ่อของเตชินกำลังนั่งดูข่าวการเมืองอยู่ เตชิน เดินเข้ามาช้า ๆ และนั่งลงที่โซฟาด้านข้าง "
    stop sound
    show chinbed
    play sound "cs3 t1.mp3"
    chin "...พ่อครับ ผมขอคุยด้วยได้ไหมครับ"
    stop sound
    show dad
    dad "..."
    play sound "cs3 t2.mp3"
    chin "…พ่อจำวันประกาศผลสอบได้ไหมครับ"
    stop sound
    dad "..."
    play sound "cs3 t3.mp3"
    chin "ผมสอบติด ... แต่สิ่งที่ผมอยากรู้ตอนนั้นไม่ใช่ผลสอบผมแค่อยากรู้ว่าแม่อยู่ไหน ... "
    stop sound
    play sound "cs3 t4.mp3"
    chin "แต่พอรู้ ก็เหมือนว่าอยู่ดี ๆ ฟ้าก็ถล่มลงมา "
    stop sound
    play sound "cs3 dad_1.mp3"
    dad "แม่แกไม่อยากให้แกเครียดก่อนสอบ"
    stop sound
    play sound "cs3 t5.mp3"
    chin "แม่ไม่อยาก หรือพ่อไม่อยากกันแน่ครับ"
    stop sound
    dad "..."
    play sound "cs3 t6.mp3"
    chin " ผมพยายามคิดว่าพ่ออยากให้ผมมีอนาคตที่มั่นคง…แต่ตอนนั้น 
    \nผมแค่อยากเจอแม่ แค่นั้นเอง...มันมากไปเหรอครับ ? "
    stop sound
    play sound "cs3 t7.mp3"
    chin "ผมไม่ได้รู้เลยว่าแม่ป่วย ไม่รู้ด้วยซ้ำว่าแม่ไม่อยู่แล้ว 
    \n... ผมไม่ทันได้ลาหรือแม้แต่พูดอะไรกับแม่เลย "
    stop sound
    play sound "cs3 t8.mp3"
    chin "แล้วพ่อยังพูดว่า ถ้าเรียนไม่จบ จะไม่ให้ผมอ่านสมุดบันทึกของแม่อีก 
    \nผมทำอะไรผิดขนาดนั้นเลยเหรอครับ"
    stop sound
    play sound "cs3 dad_2.mp3"
    dad "พ่อคิดว่ามันดีที่สุดสำหรับตอนนั้น พ่อไม่อยากให้เรื่องแม่ทำให้แกหมดกำลังใจ 
    \nเพราะพ่อเชื่อว่าแกต้องทำได้"
    stop sound
    play sound "cs3 t9.mp3"
    chin "แต่พ่อไม่ถามเลย ... ว่าสิ่งที่ผมต้องการคืออะไร พ่อคิดว่า ความคิดพ่อถูกเสมอ"
    stop sound
    play sound "cs3 t10.mp3"
    chin "วันนั้นผมแค่อยากได้คำปลอบใจ อยากได้คนที่รู้สึกเศร้าไปด้วยกันกับผม 
    \nผมอยากได้พ่อที่คอยรับฟังและไม่ตัดสินใจแทนผม"
    stop sound
    play sound "cs3 dad_3.mp3"
    dad "พ่อจะพูดตรง ๆ นะพ่อไม่รู้ว่าหน้าที่พ่อคืออะไร พ่อเพิ่งเคยเป็นพ่อคน 
    \nแค่คิดว่าควรวางแผนอนาคตให้แต่พ่อควรจะถามความเห็นของแก 
    \nไม่ใช่คิดแทนสินะ พ่อจะพยายามเปลี่ยนละกัน "
    stop sound
    play sound "cs3 t11.mp3"
    chin "…ผมยังไม่ให้อภัยพ่อหรอกครับ
    \nแต่ ... ผมจะพยายามเข้าใจพ่อ"
    stop sound
    hide chinbed
    hide dad
    scene black with Fade(0.5, 0.5, 0.5)
    jump university_class4

# บทที่ 7
label university_class4:
    scene bg class with dissolve
    play sound "7sup1.mp3"
    "ณ ตึกอาคารเรียนรวมของมหาวิทยาลัย นักศึกษาต่างพากันเดินเข้าห้องเรียน 
    \nซึ่งมีอาจารย์ยืนอยู่หน้าชั้นพร้อมเอกสารในมือ บรรยากาศภายในห้อง
    \nเต็มไปด้วยเสียงพูดคุยจอแจของนักศึกษาที่กำลังเตรียมตัว "
    stop sound
    scene classroom with dissolve
    show aj2
    play sound "อาจารย์_2_7.mp3"
    aj "วันนี้เรานัดกันว่าแต่ละกลุ่มจะแสดงบทบาทสมมุติใช่ไหมคะ หัวข้อคือ ความสัมพันธ์ในครอบครัว
    \nเป้าหมายของกิจกรรมนี้คือการสะท้อนความรู้สึกและมุมมองที่มีต่อครอบครัว 
    \nอาจารย์ให้เวลาพวกเราเตรียมตัว 10 นาที แล้วจะสุ่มเรียกนะ เพื่อความเท่าเทียม"
    stop sound
    hide aj2
    scene bg class with dissolve
    play sound "7sup2.mp3"
    "นักศึกษาหลายกลุ่มเริ่มขยับเก้าอี้ เตรียมบทและซักซ้อมกันเป็นครั้งสุดท้าย 
    \nเสียงหัวเราะคละเคล้ากับความตื่นเต้น บางกลุ่มดูมั่นใจ ขณะที่บางกลุ่มยังลังเลกับบทพูดที่เขียนไว้"
    stop sound
    show may
    play sound "7m1.mp3"
    npc "สุ่มเรียกแหละ ตื่นเต้นจัง"
    stop sound
    show player_b
    b "เรามาซ้อมบทกันอีกรอบเถอะ"
    play sound  "7m2.mp3"
    npc "ชิน…เธอพร้อมหรือยัง ?"
    stop sound
    show chinr
    play sound "7t1.mp3"
    chin "อืม ก็คงต้องพร้อมอะ"
    stop sound
    hide may
    hide player_b
    hide chinr
    scene classroom

    menu:
        "ลองทำเต็มที่เหมือนที่ซ้อมมาก็พอ":
            show chinc
            play sound "7tQ1_0.mp3"
            chin "ก็จริง…งั้นไปกันเถอะ "
            stop sound
            hide chinc
            jump question_7_2

        "ไม่ต้องกังวลนะ เราอยู่ตรงนี้กับเธอ":
            show chinc
            play sound "7tQ1_+1.mp3"
            chin "... อืม ขอบใจนะ "
            stop sound
            hide chinc
            jump question_7_2

        "อย่าทำเสียหน้าเพื่อนนะ ทุกคนรอดูอยู่":
            show chinc
            play sound "7tQ1_-1.mp3"
            chin "... อืม"
            stop sound
            hide chinc
            jump question_7_4

label question_7_2:
    menu:
        "เธอซ้อมมาดีแล้ว เชื่อสิว่าเธอทำได้":
            show chinc
            play sound "7tQ2_+1.mp3"
            chin "…โอเค จะพยายาม "
            stop sound
            hide chinc
            jump question_7_3

        "ถ้าตื่นเต้นขนาดนี้ เดี๋ยวพลาดอีกหรอก":
            show chinc_n
            play sound "7tQ2_-1.mp3"
            chin "… อย่ากดดันสิ "
            stop sound
            hide chinc_n
            jump question_7_4

        "เดี๋ยวก็ผ่านไปแป๊บเดียวเอง":
            show chinc
            play sound "7tQ2_0.mp3"
            chin "อืม…หวังว่าจะเป็นแบบนั้น "
            stop sound
            hide chinc
            jump question_7_3

label question_7_3:
    menu:
        "พูดตามที่ซ้อมไว้ก็พอ ไม่ต้องคิดเยอะ":
            show chinc_n
            play sound "7tQ3_0.mp3"
            chin "ได้ … 
            \nบทพ่อ : ก็เพราะพ่ออยากให้ลูกมีอนาคตที่มั่นคง"
            stop sound
            hide chinc_n
            jump question_7_5

        "อย่าหยุดสิ พูดตามบทไป":
            show chinca
            play sound "7tQ3_-1.mp3"
            chin "บทพ่อ : ก็เพราะพ่ออยากให้ลูกมีอนาคตที่มั่นคง "
            stop sound
            hide chinca
            jump question_7_6
            
        "พูดตามใจเธอเลย ไม่ต้องตามบทเป๊ะก็ได้ เดี๋ยวเราช่วย":
            show chinc
            play sound "7tQ3_+1.mp3"
            chin "... อืม ขอบใจนะ
            \n บทพ่อ : ที่พ่อทำแบบนี้เพราะ พ่ออยากให้ลูกมีอนาคตที่มั่นคง"
            stop sound
            hide chinc
            jump question_7_5

label question_7_4:
    show may
    play sound "7mQ4.mp3"
    npc "ไม่เป็นไรนะ ทำเท่าที่ทำได้ก็พอ"
    stop sound
    hide may

    menu:
        "ง่าย ๆ เอง ไม่ต้องคิดมาก":
            show chinc_n
            play sound "7tQ4_-1.mp3"
            chin "…เข้าใจแล้ว "
            stop sound
            hide chinc_n
            jump question_7_7
            
        "ใช่ ทำให้ดีที่สุดก็พอแล้ว":
            show chinc
            play sound "2tQ1_0.mp3"
            chin "…อืม"
            stop sound
            hide chinc
            jump question_7_6

        
    
label question_7_5:
    scene classroom
    show player_b
    b "บทลูก : หนูกลัวว่าจะทำได้ไม่ดี…"
    show chinc
    play sound "7tQ5.mp3"
    chin "บทพ่อ : แค่ทำให้ดีที่สุดก็พอ "
    stop sound
    hide player_b
    hide chinc

    menu:
        "เดี๋ยวก็ผ่านไปแป๊บเดียวเอง":
            show chinc
            play sound "7tQ5_01.mp3"
            chin "…อืม งั้นลองตามบทก็ได้  "
            stop sound
            play sound "7tQ5_02.mp3"
            chin "บทพ่อ : พ่ออาจกดดันไปบ้าง แต่พ่อก็ห่วงลูกนะ"
            stop sound
            hide chinc
            jump question_7_8
            
        "ค่อย ๆ พูดออกมาตามที่คิดจริง ๆ ก็ได้นะ":
            show chinc
            play sound "7tQ5_+1.mp3"
            chin "บทพ่อ : พ่ออาจกดดันไปบ้าง แต่จริง ๆ พ่อก็ห่วงลูกนะ "
            stop sound
            hide chinc
            jump question_7_8

        "จะเงียบอีกนานไหม เร็วเข้าสิ":
            show chinc_n
            play sound "7tQ5_-1.mp3"
            chin "บทพ่อ : พ่ออาจกดดันไปบ้าง แต่พ่อก็ห่วงลูก"
            stop sound
            hide chinc_n
            jump question_7_7

label question_7_6:
    menu:
        "อีกนิดเดียวก็จะจบแล้ว":
            show chinc
            play sound "7tQ6_0.mp3"
            chin "…อืม จะพยายาม"
            stop sound
            hide chinc
            jump question_7_8
            
        "เธอทำได้ดีแล้วนะ":
            show chinc
            play sound "7tQ6_+1.mp3"
            chin "… ขอบใจ "
            stop sound
            hide chinc
            jump question_7_8

        "อย่าพลาดนะ":
            show chinc_n
            play sound "7tQ6_-1.mp3"
            chin "… อืม"
            stop sound
            hide chinc_n
            jump question_7_7

label question_7_7:
    menu:
        "พักหายใจก่อน เดี๋ยวเริ่มกันใหม่นะ":
            show chinc
            play sound "7tQ7_0.mp3"
            chin "… โอเค "
            stop sound
            hide chinc
            jump question_7_9

        "ไม่ไหวก็อย่าฝืนเลยดีกว่า":
            show chinc_n
            chin "..."
            hide chinc_n
            jump bad_ending7
    
label question_7_8:
    show player_b
    b "บทลูก : จริงเหรอครับ ผมคิดว่าพ่ออยากให้ผมเก่งที่สุดทุกเรื่อง"
    show chinc
    play sound "7tQ8.mp3"
    chin "บทพ่อ : พ่อแค่อยากให้ลูกเอาตัวรอดได้ถ้าพ่อไม่อยู่"
    stop sound
    hide player_b
    hide chinc

    menu:
        "เห็นไหม ไม่ได้ยากอะไรเลย ทำไมต้องกังวลนัก":
            show chinc_n
            play sound "7tQ8_-1.mp3"
            chin "… อือ "
            stop sound
            hide chinc_n
            jump question_7_9
            
        "ดีมาก เธอพูดเป็นธรรมชาติมากเลย":
            show chinc
            play sound "7tQ8_+1.mp3"
            chin "…ขอบใจนะ รู้สึกเบาขึ้น "
            stop sound
            hide chinc
            jump good_ending7
        
        "จบไปด้วยดีแล้วนะ":
            show chinc
            play sound "7tQ8_0.mp3"
            chin "…อืม อย่างน้อยก็ผ่านไปได้"
            stop sound
            hide chinc
            jump normal_ending7

label question_7_9:
    show aj2
    play sound "อาจารย์_2_9.mp3"
    aj "โอเคค่ะ กลุ่มต่อไปออกมาได้เลย"
    stop sound
    hide aj2
    
    menu:
        "ครั้งหน้าก็อย่าทำให้กังวลอีกล่ะ":
            show chinc_n
            chin "..."
            hide chinc_n
            show aj2
            play sound "อาจารย์_21_end.mp3"
            aj "ตลอดภาคเรียนที่ผ่านมา เราได้เรียนรู้ถึงความสัมพันธ์ในรูปแบบต่าง ๆ ไม่ว่าจะเป็นครอบครัว
            \nเพื่อน หรือสังคมรอบตัว จากการแสดงของทุกกลุ่มที่ผ่านมาอาจารย์มั่นใจว่า การเรียนรู้ที่ทุกกลุ่มได้รับตรงกัน"
            stop sound
            play sound "อาจารย์_22_end.mp3"
            aj "คือความสัมพันธ์ที่ดี ในทุกความสัมพันธ์สิ่งสำคัญคือการได้เข้าใจความรู้สึกของกันและกัน และรู้จักให้พื้นที่ความเป็นส่วนตัวอย่างเหมาะสม
            \nหวังว่าสิ่งที่ทุกคนได้เรียนรู้จะช่วยสร้างความสัมพันธ์ในทุก ๆ ความสัมพันธ์ได้เป็นอย่างดี ขอบคุณค่ะ"
            stop sound
            hide aj2
            jump bad_ending7
        
        "เธอทำได้ดีนะ เหมือนพูดจากใจเลย":
            show chinc
            play sound "7tQ9_+1.mp3"
            chin " ... รู้สึกโล่งขึ้นเลย"
            stop sound
            hide chinc
            show aj2
            play sound "อาจารย์_21_end.mp3"
            aj "ตลอดภาคเรียนที่ผ่านมา เราได้เรียนรู้ถึงความสัมพันธ์ในรูปแบบต่าง ๆ ไม่ว่าจะเป็นครอบครัว
            \nเพื่อน หรือสังคมรอบตัว จากการแสดงของทุกกลุ่มที่ผ่านมาอาจารย์มั่นใจว่า การเรียนรู้ที่ทุกกลุ่มได้รับตรงกัน"
            stop sound
            play sound "อาจารย์_22_end.mp3"
            aj "คือความสัมพันธ์ที่ดี ในทุกความสัมพันธ์สิ่งสำคัญคือการได้เข้าใจความรู้สึกของกันและกัน และรู้จักให้พื้นที่ความเป็นส่วนตัวอย่างเหมาะสม
            \nหวังว่าสิ่งที่ทุกคนได้เรียนรู้จะช่วยสร้างความสัมพันธ์ในทุก ๆ ความสัมพันธ์ได้เป็นอย่างดี ขอบคุณค่ะ"
            stop sound
            hide aj2
            jump good_ending7
        
        "อย่างน้อยก็ผ่านไปแล้ว":
            show chinc
            play sound "7tQ9_0.mp3"
            chin "ใช่…ก็ถือว่าผ่านไปได้ "
            stop sound
            hide chinc
            show aj2
            play sound "อาจารย์_21_end.mp3"
            aj "ตลอดภาคเรียนที่ผ่านมา เราได้เรียนรู้ถึงความสัมพันธ์ในรูปแบบต่าง ๆ ไม่ว่าจะเป็นครอบครัว
            \nเพื่อน หรือสังคมรอบตัว จากการแสดงของทุกกลุ่มที่ผ่านมาอาจารย์มั่นใจว่า การเรียนรู้ที่ทุกกลุ่มได้รับตรงกัน"
            stop sound
            play sound "อาจารย์_22_end.mp3"
            aj "คือความสัมพันธ์ที่ดี ในทุกความสัมพันธ์สิ่งสำคัญคือการได้เข้าใจความรู้สึกของกันและกัน และรู้จักให้พื้นที่ความเป็นส่วนตัวอย่างเหมาะสม
            \nหวังว่าสิ่งที่ทุกคนได้เรียนรู้จะช่วยสร้างความสัมพันธ์ในทุก ๆ ความสัมพันธ์ได้เป็นอย่างดี ขอบคุณค่ะ"
            stop sound
            hide aj2
            jump normal_ending7

label good_ending7:
    show chinc
    play sound "7sup_good.mp3"
    "เตชินไม่รู้สึกโดดเดี่ยวอีกต่อไป และเริ่มเชื่อว่าตัวเองไม่จำเป็นต้องสมบูรณ์แบบ"
    stop sound
    hide chinc
    window hide
    show good7
    pause 15.0
    hide good7
    show sup6
    pause 15.0
    hide sup6
    $ score += 1
    jump check_ending

label normal_ending7:
    show chinc
    play sound "7sup_normal.mp3"
    "เตชินยังคงต่อสู้กับความรู้สึกของตัวเอง แต่ก็ไม่กลัวที่จะมองไปข้างหน้า"
    stop sound
    hide chinc
    window hide
    show normal7
    pause 15.0
    hide normal7
    show sup6
    pause 15.0
    hide sup6
    jump check_ending

label bad_ending7:
    show chinca
    play sound "7sup_bad.mp3"
    "เตชินยังไม่พร้อมเผชิญโลกภายนอก และเลือกปิดตัวเองจากผู้คน"
    stop sound
    hide chinca
    window hide
    show bad7
    pause 15.0
    hide bad7
    show sup6
    pause 15.0
    hide sup6
    $ score -= 1
    jump check_ending

#รวมคะแนน 5-6 good end , 3-4 normal end , 1-2 bad end
#เหลือทำรวมคะแนน

label check_ending:
    if score >= 5:
        jump good_ending
    elif score >= 3:
        jump normal_ending
    else:
        jump bad_ending


label good_ending:
    scene goodend1 with dissolve
    stop music
    play music "concert.mp3"
    $ renpy.music.set_volume(0.25, channel="music")
    play sound "goodend1P.mp3"
    "ที่ลานกิจกรรมที่เต็มไปด้วยแสงไฟและเสียงเพลงจากคอนเสิร์ตผู้คนโบกมือ
    \nตามจังหวะเพลง เตชินอยู่กับ ปุณ และ เมย์ทั้ง 3 คน ยืนอยู่ไม่ห่างจากเวที "
    stop sound
    scene goodend2 with dissolve
    play sound "goodend2.mp3"
    "เตชินไม่ได้หายจากภาวะซึมเศร้า ... แต่เขาเริ่มรู้ว่าเราไม่จำเป็นกดดันตัวเองมากจนเกินไป
    \nหลังผ่านเหตุการณ์ต่าง ๆ ในชีวิตจริง และได้เผชิญหน้ากับพ่อ เตชินเริ่มเปิดใจให้ผู้คนอีกครั้ง "
    stop sound
    
    scene black
    stop music
    call screen about_credits

    return

label normal_ending:
    scene normalend1 with dissolve
    play sound "normalend1P.mp3"
    "ณ ข้างลานกิจกรรม เตชินยืนอยู่กับเมย์และ ปุณ เสียงดนตรีจากเวทีคอนเสิร์ตดังแว่วมา
    \nเขาไม่ได้เข้าไปร่วมกิจกรรมด้านใน แต่ก็ยืนฟังเพลงอยู่ด้านนอก สายตามองผู้คนรอบตัวด้วยแววตาที่ไม่ปิดกั้นเหมือนแต่ก่อน "
    stop sound
    scene normalend2 with dissolve
    play sound "normalend2.mp3"
    "เตชินยังคงอยู่กับภาวะซึมเศร้า...แต่เริ่มรับมือกับมันได้มากขึ้นเขายังไม่ได้เปิดใจให้ทั้งหมด 
    \nแต่ก็ไม่ได้ปิดกั้นตัวเองเหมือนวันแรก การได้พูด การได้ยอมรับว่าเจ็บปวด 
    \nคือจุดเริ่มต้นของการรักษาและแม้เขาจะยังไม่กล้าเดินเข้าไปในแสงไฟ แต่เขาก็ไม่กลัวมันอีกต่อไป "
    stop sound
    
    scene black
    stop music
    call screen about_credits

    return


label bad_ending:
    scene badend1 with dissolve
    play sound "badend1.mp3"
    "ภายในห้องพักของเตชินที่ปิดม่านทึบ บนโต๊ะยังมีบทละครที่ถูกพับไว้ครึ่งหนึ่ง
    \nและจดหมายที่ยังไม่ได้เปิดจากพ่อมีเสียงดนตรีจากคอนเสิร์ตลอยมาจากลานกิจกรรม"
    stop sound
    scene badend2 with dissolve
    play sound "badend2.mp3"
    "ภาวะซึมเศร้าของเตชินยังคงอยู่ เขาเริ่มหลีกเลี่ยงการเข้าสังคม และไม่ได้เข้าร่วมคอนเสิร์ตที่จัดขึ้น
    \nในวันสุดท้ายของเทอม เพราะเขายังไม่สามารถเปิดใจให้กับผู้คนได้ เขาคิดเสมอว่าไม่มีใครเข้าใจเขา "
    stop sound

    scene black
    stop music
    call screen about_credits

    return