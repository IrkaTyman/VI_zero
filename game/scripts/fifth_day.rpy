label fifth_day:
    play music "music/music good.mp3" fadein fadein volume volume loop
    scene black:
        zoom 2.0
    with fade

    scene hall
    with dissolve
     
    "Сегодня я должен выяснить много информации о компании, и при этом не вызвать подозрения службы безопасности. 
    Наверняка у огромной корпорации есть такая, а может и что похуже, учитывая масштаб происходящего…"

    scene office
    with fade

    show alan at left:
        linear 0.0 xzoom -1.0 yzoom 1.0
    with dissolve

    show grace at right
    with dissolve

    "И чего это все столпились тут? Впервые вижу столько работников в одном месте."

    g "Надеюсь, что все уже пришли. Заранее отвечу на вопрос, почему я решила собрать вас тут, а не воспользовалась сервисом корпоративной связи для рассылки задач. Я хочу, чтобы вы понимали, что продукт, о котором сейчас пойдет речь, имеет более серьезное значение для всей компании, чем вам может показаться. Алан, введи всех в курс дела, пожалуйста."

    a "Конечно. Итак, один из наших проектов заинтересовал крупного заказчика. 
    Он согласился не только оплатить уже потраченную на разработку сумму, но и профинансировать дальнейшую работу и поддержку продукта. 
    Сумма, о которой идет речь, еще не фигурировала в контрактах нашей корпорации."

    a @ ce "Но куда важнее другое - от исхода работы зависит наша репутация. 
    Поэтому очень прошу вас, выложитесь так, как не выкладывались никогда. 
    С нашей стороны мы обещаем крупную премию сразу после релиза проекта."

    g @ smirk "Надеюсь, вы поняли,  что в ваших руках будущее компании. Покажите, что мое детище, структура, 
    которую я выстраивала годами, отделы, которые я во многом отбирала сама и развитие которых я контролировала день за днем, способны выйти на новый уровень качества."

    g "Вы начнете с раннего тестирования уже написанного и плавно перейдете к доработке и приведению проекта к тому виду, 
    который желает видеть наш заказчик. А теперь отправляйтесь по отделам и приступайте к работе. 
    Указания вам разошлет Алан, а о проделанной работе тимлиды будут лично отчитываться передо мной. Удачного вам дня!"

    "Нарасследовался, блин."

    scene office
    with dissolve
    play sound "music/keyboard.mp3" fadein fadein volume volume

    show karen

    k @ say "Послушайте! Я только что получила сообщение от Алана с первыми указаниями. Он пишет, что работу игры будем тестировать на нейрочипе NCC V1, 
    поэтому сегодня в офис прибудет группа добровольцев, чтобы мы могли проверить игру на различных модификациях чипов. 
    Но нужно, чтобы кто-то прямо сейчас встретил их у входа."

    k "Я спущусь, но будьте готовы, что нужно будет спуститься и помочь. "
    stop sound fadeout 2.0

    scene office
    with fade
    play sound "music/keyboard.mp3" fadein fadein volume volume

    show kai
    with dissolve

    kai @ serious "[nameM], не мог бы ты спуститься и проверить, где там застряла Карэн? Она уже должна быть здесь."
    stop sound fadeout 2.0

    "Хорошо, я посмотрю, что там происходит." 

    "Не думал, что удастся поработать с нейрочипами так скоро. Все-таки я рассчитывал пока учиться создавать простые игры, 
    но тут такой шанс погрузиться в по-настоящему популярное направление. Ведь сегодня практически каждый часы проводит в онлайн-играх нейронного типа. "
    scene elevator outside
    with dissolve
    pause 1.0

    scene elevator inside
    with dissolve
    pause 1.0

    scene hall
    with dissolve

    if (soleCompany %  7 > loveLine %  4):
        show karen at right

        show unknown at left
        k @ angry "Поймите же, вы опоздали, а теперь пытаетесь выгородить себя глупыми оправданиями, тем самым еще больше задерживая и меня, и себя, в особенности. Так может вы прекратите препираться и просто пройдете со мной наверх, чтобы наконец приступить к работе?"

        unknown @ say "Какого черта ты обвиняешь меня? Я уже объяснил, что задержался не по своей вине. Мой шофер решил объехать пробку, в итоге попав в еще большую. Теперь придется уволить его."

        k @ angry "Шофер? Да вы вообще на такси приехали. Кого вы пытаетесь из себя строить?"

        unknown "Да как ты смеешь!? Ты хоть понимаешь, кто я такой и какое одолжение делаю, выделяя вам крупицы своего золотого времени?"

        k @ say "Если бы крупицы вашего времени были бы действительно золотыми, вы бы уже проследовали за мной в отдел. А так они больше напоминают песок."

        unknown @ say "А ты совсем не сообразительная, оказывается!"

        "Успокойтесь. Вы в себе вообще, как вы могли замахиваться на незнакомого человека?"

        unknown @ say "А? Ты еще кто черт возьми такой? Может мне и тебя нужно научить хорошим манерам?"

        k @ angry  "Хватит! Пора остановить это безумие. Просто выполните свою работу и возвращайтесь к привычным делам."

        unknown @ say "Всенепременно."

    else:
        show unknown 
        # rewrite
        unknown "AAAAAAaAAAaAAaaaaaaaaAAAAaaAAAAAaaaaAAAa"
        hide unknown 

        show karen
        with dissolve
        k @ say "Я не знаю, что и делать. Он один остался. Элли пытается успокоить его и отправить в отдел, но он никак не остановится. Заладил, что мы не оказываем ему должного уважения, поэтому он не сдвинется с места."

        "Я попытаюсь разобраться."
        hide karen

        show unknown at left
        with dissolve
        show elly at right
        with dissolve

        unknown "Повторяю вам, я не начну работать, пока вы не встретите меня, как этого подобает мой статус."
        e "Простите, но мы не можем по-особенному встречать каждого из десятков тестировщиков наших продуктов. К тому же, вы опоздали, создав тем самым проблему для меня и себя."
        
        unknown @ say "Да как ты смеешь обвинять меня!? Если я сейчас развернусь и уйду, как же вы будете искать еще кого-то с новейшим NCC V1.5? 
        А я отвечу: никого вы не найдете. Так что меньше пренебрежительного тона и больше уважения, девчонка!"

        "Да как вы можете вести себя так с незнакомой девушкой?"

        e "Нет, [nameM]! Остановись! Мы не можем поступать с ним так. Я не верю, что ты способен уподобиться ему."

        "Прости, Элли. Но я не мог уже оставаться спокойным. Ты права, нужно просто сопроводить его до отдела. Так что вы без вопросов идешь с нами, договорились?"

        unknown "Как же вы мне надоели. Ведите, надеюсь там я смогу высказать все вашему непутевому начальству."

    scene black:
        zoom 2.0
    with fade

    scene testing department
    with dissolve 

    show karen
    with dissolve

    k @ say "Это Виктор. Упрямый тип. Но нам без него действительно никуда, слишком уж редкий у него нейрочип. Пока таких ни у кого нет, ранний прототип. Но если хотим играть на опережение, то нужно адаптировать игру и для следующего поколения чипов. Так что придется потерпеть. Кажется, тестирование начинается."

    "А разве это не Грейс с Аланом в комнате вон там? Место кажется неприметным, но оттуда все должно быть прекрасно видно."

    k "И правда они. Видимо, проект действительно серьезный, раз Грейс сама решила все контролировать."


    scene black:
        zoom 2.0
    with fade
    pause 2.0

    scene testing department
    with dissolve 

    show karen at right
    k @ smile "Ну, что скажете? Какие первые эмоции, хорошее ли было соединение?"

    show unknown happy at left
    with dissolve

    v "Просто восхитительно! По-другому сложно описать те невероятные ощущения, что я испытывал эти несколько часов."

    k @ say "Может, какие-то претензии есть? Недочеты?"

    v "Знаете, я бы за дневной эпизод извиниться хотел. Сам не знаю, что на меня нашло."

    k "Я все-таки имела ввиду игру…"

    v "Игру? А, с игрой все просто замечательно. Никаких претензий, я с радостью приеду на еще один сеанс тестирования."

    k @ say "Хорошо, будем знать. Тогда пройдемте к выходу, нужно будет заполнить несколько бумаг."
    hide karen
    with dissolve
    hide unknown
    with dissolve

    "Что это с ним вообще? Это совсем другой человек! Где тот грубый человек, что готов был в драку полезть на пустом месте?"

    if (soleCompany % 7 <= loveLine % 4):
        "У меня есть кое-какая догадка, связанная с новым проектом и тайной деятельностью корпорации. Напишу Элли, чтобы пришла в отдел тестирования после окончания рабочего дня"

        scene black
        with dissolve
        pause 0.5

        scene testing department
        with dissolve
        show elly
        e @ disbelief "Так что ты хотел рассказать?"

        "Возможно, использование нейрочипа для игр как-то воздействует на человека. Я не до конца понимаю, но нужно это проверить."

        e @ disbelief "Ты собрался включать систему? Может быть не стоит? Я волнуюсь за тебя…"

        "Другого способа получить ответы просто нет."

        # rewrite (про себя)
        "Я должен сконцентрироваться на отрицательных эмоциях. Как он кричал на Элли. Ее испуганное лицо. Слезы."

        stop music fadeout fadeout
        pause fadeout
        play music "music/music bad.mp3" volume volume

        jump splashscreen2
        return
    
    jump fifth_day_continue
    return

label splashscreen2:
    image splash = "intro/first.png"
    image blackIm = "intro/black.png"
    image enterPressed = "intro/center_text.png"

    show splash with dissolve
    $ renpy.pause(3.0)

    show blackIm with dissolve
    $ renpy.pause(2.0)

    show enterPressed at truecenter
    with dissolve 
    
    call screen keypress2

    return

screen keypress2():
    key "K_SPACE" action Jump("succeeded2")
    timer 4.0 action Jump("splashscreen2")

label succeeded2:
    image loader0 = "intro/loader (0).png"
    image loader1 = "intro/loader (1).png"
    image loader2 = "intro/loader (2).png"
    image loader3 = "intro/loader (3).png"
    image loader4 = "intro/loader (4).png"
    image loader5 = "intro/loader (5).png"
    image loader6 = "intro/loader (6).png"
    image loader7 = "intro/loader (7).png"
    image loader8 = "intro/loader (8).png"
    image loader9 = "intro/loader (9).png"
    image loader10 = "intro/loader (10).png"
    image loader11 = "intro/loader (11).png"

    show loader0 at right
    pause 0.3
    show loader1 at right
    pause 0.3
    show loader2 at right
    pause 0.3
    show loader3 at right
    pause 0.3
    show loader4 at right
    pause 0.3
    show loader5 at right
    pause 0.3
    show loader6 at right
    pause 0.3
    show loader7 at right
    pause 0.3
    show loader8 at right
    pause 0.3
    show loader9 at right
    pause 0.3
    show loader10 at right
    pause 0.3
    show loader11 at right
    pause 4.0
    jump fifth_day_cont2
    return

label fifth_day_cont2:
    scene black:
        zoom 2.0
    with dissolve 
    pause 1.0

    scene testing department
    with dissolve 

    show elly
    e @ sad "[nameM], ты как? Все закончилось."

    "Эмоции. {w}Отрицательные эмоции. {w}Виктор. {w}Элли. {w}Но что? {w}Что я чувствовал?"

    e @ sad "Ты в порядке? Выглядишь странно."

    "Элли, я не могу почувствовать гнев!"

    e "Но это же хорошо?"

    "Если бы только это не было эффектом от использования нейрочипа для игр. Ты понимаешь, что это означает?"

    e  "Кажется, картинка начинает складываться… Правительственное финансирование, подавление негативных эмоций. Но это игра по-крупному! Что же нам делать?" 
        
    e @ surprised "Что ТЫ собираешься делать?"

    menu:
        "Мы должны рассказать всем правду":
            jump fifth_day_continue
            return

        "Слишком опасно продолжать, мы рискуем всем":
            jump fifth_day_continue
            return

label fifth_day_continue:
    if (soleCompany %  7 <= loveLine % 4):

        show elly at right 
        with move

        show alan at left:
            linear 0.0 xzoom -1.0 yzoom 1.0
        with dissolve

        a @ smile "Поздравляю, вам удалось поразить меня вашей упертостью!"

        "Что!? С каких пор он тут?"

        e @ surprised "Я не знаю!"

        a "Может, у вас есть какие-то идеи на счет того, что мне с вами делать? Вы же узнали так много… 
        Вот только не говорите, что будете жить и работать дальше, делая вид, будто не знаете о настоящей деятельности корпорации." 
        
        a @ ce "Вы наверняка уже все поняли: правительство платит нам за разработку игр для нейрочипов в наших секретных отделах. 
        Да-да, Элли, в один из таких отделов ты и попала, продемонстрировав верность компании на протяжении нескольких лет работы."
        
        "Конечно, ты еще не успела начать разрабатывать игры для чипов, но, как я вижу, вы разгадали основную их направленность - 
        маскируясь под сервис взаимодействия игры и разума, программа отправляет сигналы надпочечникам, 
        останавливая на время выработку адреналина и норадреналина, тем самым нейтрализуя агрессивное поведение человека."

        a @ smile "Именно эту полезную функцию ученые обнаружили на ранних этапах создания технологии Neuroconnect и чипов NCC V1."

        "Но это же прямое нарушение свободы, нарушение всех существующих законодательств, всех моральных норм в конце концов!"

        a @ smile "Моральные нормы? Миллионы мошенников, воров, убийц и насильников ежедневно выходят на улицы, уставшие от бедности, проблем с головой и другими вечными спутниками всех несчастных. Мы же самым безобидным путем снижаем преступность по всему миру, взамен требуя лишь сумму от государства. Скажи, кто же здесь проигрывает?"

        "Кто проигрывает? Личность, природа человека - вот кто проигрывает! Какие бы ужасные преступления не совершались день изо дня - ваши методы идут против самих основ человеческой сущности."

        a @ smile "Это каждый решает сам для себя. Но пока общество не знает об этом, нет никакой необходимости в размышлениях о таких глубоких вещах. 
        Я дам тебе другой вопрос для размышления. Вариант первый: ты продолжаешь твердить про свободу и природу, 
        никак не идешь нам на встречу и… твое будущее гарантировано не будет таким, каким ты себе его представлял."
        
        a "Вариант второй: ты подписываешь соглашение о неразглашении, навсегда забываешь о всех возникших внутри тебя противоречиях, 
        а мы даем тебе продвижение по карьерной лестнице и работу в секретном отделе."
        a @ smile "Раз уж тебе так приглянулась Элли, можешь даже попасть в ее команду. Что скажешь?"

        "Хотите купить меня рассказами об обеспеченном будущем? Думаете такая цена у моих принципов?"

        e @ sad "[nameM], прекрати пожалуйста! Ты же понимаешь, что у нас нет выбора. Хотя бы ради меня, согласись на сделку."

        'Элли, я правда не знаю, как должен поступить.'

        e @ sad "Умоляю, давай сохраним это как нашу общую тайну и продолжим жить дальше."

        a @ smile "А девушка оказалась более сообразительной. Достаточно бессмысленных рассуждений, вот бумаги. Прочти и подпиши."
     
        "Хорошо… Похоже, другого выхода нет."

        scene coffee house
        with dissolve

        show elly
        with dissolve

        "Скажешь что-нибудь?"

        e @ sad "У меня так много мыслей, что ни одну я не могу сформулировать. Думаешь, мы сильно влипли? Теперь они от нас не отстанут?"

        show elly at right
        with move

        show lloyd at left:
            linear 0.0 xzoom -1.0 yzoom 1.0

        ar @ month_wide "Ооо, еще как не отстанут! Вижу, вы выбрали  путь смирения. Что же, вас можно понять… Но я не смог пойти на сделку с совестью, и вот я здесь."

        "Арон? Только теперь я понимаю, что все твои странные слова вовсе не были бредом. Но разве тебе не грозит опасность, если ты не стал подписывать соглашение и так свободно разгуливаешь по разным заведениям?"

        ar @ smile_wide_ce "Если знаешь, когда нужно исчезнуть, а когда можно появляться, то проблем не так много."

        "Значит выход все-таки был… А я запаниковал и посчитал сделку единственным выходом."

        ar "Послушай, ты все еще можешь остаться достойным человеком. Давай соберем доказательства незаконной деятельности корпорации по заказу государства и разошлем по всем доступным независимым СМИ, распространим в интернете."

        e @ surprised "Нет! Мы уже согласились молчать, и не станем нарушать соглашение."

        ar  @ smile_angry_wide_ce "Девочка, ты действительно считаешь, что в этой игре соблюдают правила? Разве ты еще не поняла?"

        "С каких пор ты решаешь, как я поступлю? Арон, я в деле."

        e @ sad "Но [nameM]! Пожалуйста, давай не будем соглашаться на такие опасные авантюры."

        "Решай за себя. Но я готов рискнуть."

        ar @ smile_wide "Отлично. Тогда завтра постарайся заняться этим. И нужно обязательно обменяться контактами для экстренной связи."

        "Согласен. Вот мой аккаунт. Тогда до завтра, увидимся."

        ar @ ce "Удачи. И будь осторожен."

        scene street way home evening
        with dissolve

        show elly 

        e @ sad ". . ."

        "Мне не нравится, что мы не можем друг друга понять. Я же никак не давлю на тебя. Почему ты считаешь правильным давить на меня?"

        e @ sad "Я волнуюсь за тебя. Мы только нашли решение, которое хоть как-то гарантирует нам безопасность, но ты тут же отказываешься от него."

        "Но как же совесть, Элли? Как мне смотреть в зеркало после такого?"

        e @ angry "А что, если смотреть в зеркало будет уже некому?"

        "Я не сверну. Прости."
        jump results_label
        return
        
    else:
        "Возможно, использование нейрочипа для игр как-то воздействует на человека. Я не до конца понимаю, но нужно это проверить."

        scene black:
            zoom 2.0
        with dissolve 
        pause 1.0

        scene testing department
        with dissolve 

        "Другого способа получить ответы просто нет. Я должен сконцентрироваться на отрицательных эмоциях. Как Виктор кричал на Карэн. Ее испуганное лицо. Его рука, едва не ударившая Карэн."

        stop music fadeout fadeout
        pause fadeout
        play music "music/music bad.mp3" volume volume loop
        jump splashscreen3

        return


label splashscreen3:
    image splash = "intro/first.png"
    image blackIm = "intro/black.png"
    image enterPressed = "intro/center_text.png"

    show splash with dissolve
    $ renpy.pause(3.0)

    show blackIm with dissolve
    $ renpy.pause(2.0)

    show enterPressed at truecenter
    with dissolve 
    
    call screen keypress3

    return

screen keypress3():
    key "K_SPACE" action Jump("succeeded3")
    timer 4.0 action Jump("splashscreen3")

label succeeded3:
    image loader0 = "intro/loader (0).png"
    image loader1 = "intro/loader (1).png"
    image loader2 = "intro/loader (2).png"
    image loader3 = "intro/loader (3).png"
    image loader4 = "intro/loader (4).png"
    image loader5 = "intro/loader (5).png"
    image loader6 = "intro/loader (6).png"
    image loader7 = "intro/loader (7).png"
    image loader8 = "intro/loader (8).png"
    image loader9 = "intro/loader (9).png"
    image loader10 = "intro/loader (10).png"
    image loader11 = "intro/loader (11).png"

    show loader0 at right
    pause 0.3
    show loader1 at right
    pause 0.3
    show loader2 at right
    pause 0.3
    show loader3 at right
    pause 0.3
    show loader4 at right
    pause 0.3
    show loader5 at right
    pause 0.3
    show loader6 at right
    pause 0.3
    show loader7 at right
    pause 0.3
    show loader8 at right
    pause 0.3
    show loader9 at right
    pause 0.3
    show loader10 at right
    pause 0.3
    show loader11 at right

    jump splashscreen3_cont
    pause 4.0

label splashscreen3_cont:

    scene black:
        zoom 2.0
    with dissolve 
    pause 1.0

    scene testing department
    with dissolve 

    "Вот все и закончилось. {w}Я должен подумать об эмоциях. {w}Отрицательных эмоциях.{w} Виктор.{w} Карэн. {w}Но что? "
    "Что я чувствовал? Я не могу почувствовать гнев!"
    "Это означает… {w}Игры нашей компании взаимодействуют с нейрочипами и подавляют эмоции? {w}Но как такое вообще возможно? Почему все молчат?" 
    "Я должен как можно скорее обсудить все с командой, уверен, что они помогут, мы найдем какой-то ответ."

    scene office evening
    with dissolve

    show kai at left
    with dissolve

    show karen at right 
    with dissolve

    "Карэн, нет времени объяснять. Я столкнулся с чем-то необъяснимым, кроме вас с Каем мне больше некому об этом рассказать. Не могла бы ты его позвать."

    k @ say "Что за срочность то такая? Могу,конечно."

    kai @ surprise "Ты уже вернулся? Зачем меня позвали?"

    "Я должен рассказать вам о том, что выяснил, наблюдая за поведением Виктора сегодня. 
    Карэн, ты помнишь, как груб этот человек был утром. Но каково же было мое удивление, когда после тестирования он стал безобиднее младенца. 
    Наоборот, он стал доброжелательным." 
    
    "Тогда я проверил работу игры на себе, и с ужасом обнаружил, что после сеанса я действительно не могу испытывать отрицательные эмоции. 
    Что-то во взаимодействии чипа с игрой заставляет разум подавлять гнев!"

    kai @ angry "Ты хоть понимаешь, куда полез? Обвиняешь компанию в чем-то незаконном? Тебе был дан шанс, а ты не справляешься даже с элементарной задачей не совать свой нос, куда не нужно."

    k "Кай, он поделился серьезной информацией относительно нашего самого приоритетного на данный момент проекта. 
    Не время разбираться, нарушил ли он должностные полномочия, решив проверить теорию на себе. 
    Для начала, мне нужно увидеть все самостоятельно."

    kai @ angry "Нет! Ты не будешь ничего проверять самостоятельно. Вообще никто и ничего не будет делать без приказа свыше. С вами свяжутся завтра, а сейчас отправляйтесь домой."

    k @ angry "Ты уверен, что ничего не перепутал? Отдел руковожу пока что я."

    kai @ ce "Проверь сообщения."

    k @ scared "Сообщение от Алана. Пишет, что завтра вызывает к себе. Так значит ты уже успел все ему передать?"

    k @ angry "Не думала, что ты…"

    kai @ smile "Я предупреждал. Нужно было заниматься только своими непосредственными обязанностями. Завтра все выяснится."

    hide kai 

    show karen 
    
    k @ angry "И в какой момент все так сильно перевернулось? Или это я была так слепа все время, что не нашла шестерку руководства прямо перед собой?"

    "Не вини себя. Ты не сделала ничего плохого, так что и отвечать тебе не за что. Я ухожу домой, увидимся."

    scene street way home evening
    with dissolve

    menu:
        "И все же мне не справиться без помощи Карэн":
            "И все же один в поле не воин. Я уверен, что она тоже хочет докопаться до правды. Но уже очевидно, что Кай будет бороться за интересы корпорации. Так что дождусь, когда Карэн выйдет из офиса, и вместе с ней в каком-нибудь тихом месте все обсудим."

            pause 1.0
            show karen

            k @ say "Ты кого-то ждешь?"

            "Да. Тебя. Давай сядем где-нибудь, где лишние уши не будут представлять опасности, например, в кофейне."

            k @ angry "Ладно, я согласна, что нельзя все это просто так оставлять."

            scene cafee2
            with dissolve

            show karen

            "Итак, я думаю, что спорить ты не будешь - Кай работает на корпорацию, и не первый день."
            
            k @ angry "Как бы мне больно не было это признавать, но все действительно так."

            "Касательно чипов и нейронных игр. Ты согласна, что мы должны как-то рассказать об этом другим?"

            k @ say "Я не уверена, что мы будем в безопасности после этого. Но работать в компании, подпольно выполняющей заказы государства, я точно не хочу. Только как мы можем повлиять на ситуацию?"

            show karen at right
            show lloyd at left
            with dissolve

            ar @ ce "Я помогу вам."

            "Арон? Только теперь я понимаю, что все твои странные слова вовсе не были бредом. Но разве тебе не грозит опасность, если ты так свободно разгуливаешь по разным заведениям?"

            ar @ ce "Если знаешь, когда нужно исчезнуть, а когда можно появляться, то проблем не так много."

            "Ты сказал, что можешь помочь."

            ar @ smile_angry_wide_ce "Давай соберем доказательства незаконной деятельности корпорации по заказу государства и разошлем по всем доступным независимым СМИ, распространим в интернете."

            k @ say "У тебя есть какие-то связи?"

            ar @ smile_wide "Да, это оставьте на меня. Ваша часть - добыть материал. Справитесь?"

            k "Я в деле."

            "Я тоже. Тогда завтра мы ищем все, что только можем найти, и связываемся с тобой."

            k @ say "Я попробую аккуратно расспросить своих знакомых в компании."

            ar "Вот мой аккаунт, для экстренной связи. Вы уже должны были понять, что доверять больше нельзя никому."

            "Тогда до завтра."

            k "Пока-пока."

            ar @ surprise "Берегите себя."
            jump results_label
            return

        "Я не могу впутывать Карэн в это опасное расследование":
            "Все-таки я не имею права подвергать Карэн такому риску. Я сам сделал выбор между идеалами и спокойной жизнью, у нее же такого выбора не было. Отправлюсь в кофейню и решу, как поступить."

            scene coffee house
            with dissolve

            show lloyd
            with dissolve

            ar @ smile_wide "Привет-привет. Чего такой грустный тут сидишь?"

            "Арон? Только теперь я понимаю, что все твои странные слова вовсе не были бредом. Но разве тебе не грозит опасность, если ты так свободно разгуливаешь по разным заведениям?"

            ar @ ce "Если знаешь, когда нужно исчезнуть, а когда можно появляться, то проблем не так много."

            "Ты сказал, что можешь помочь."

            ar @ smile_angry_wide_ce "Давай соберем доказательства незаконной деятельности корпорации по заказу государства и разошлем по всем доступным независимым СМИ, распространим в интернете."

            "Я в деле. У тебя есть связи для этого?"

            ar @ smile_wide "Да, это оставь мне. Твоя часть - добыть материал. Справишься?"

            "Я сделаю все возможное."

            ar "Отлично. Тогда завтра постарайся заняться этим. И нужно обязательно обменяться контактами для экстренной связи."

            "Согласен. Вот мой аккаунт. Тогда до завтра, увидимся."

            ar @ surprise "Удачи. {w}И будь осторожен."


            scene street way home evening
            with dissolve
            play sound "music/music good.mp3" fadein fadein volume volume loop


            "Сегодняшний день перевернул все с ног на голову. Но судьба человека определяется его способностью сопротивляться внешним угрозам. Я преодолею препятствия и сделаю тайное явным."
            stop sound fadeout 3.0
            jump results_label
            return

label results_label:
    scene black:
        zoom 2.0
    with fade

    scene hall
    with dissolve

    show alan
    with dissolve

    a "Доброе утро, [nameM]. Пройдем до моего кабинета, нам есть, что обсудить."

    "Разве? Боюсь, я не в том положении, чтобы отказывать вам."
    
    # rewrite (про себя)
    "И чего он хочет? Так быстро прознал о моих вчерашних планах? Но как?"

    scene secret office empty
    with dissolve
    pause 1.0

    scene testing department
    with dissolve      

    show alan at left:
        linear 0.0 xzoom -1.0 yzoom 1.0
    with dissolve 

    show grace at right
    with dissolve

    g @ smirk "Мы не знакомы, молодой человек. Но я уверена, что ты знаешь, кто я и как стала тем, кем являюсь. 
    Как ты думаешь, какую цену платит тот, кто хочет вписать свое имя в страницы истории?" 

    hide alan

    show grace
    with dissolve
    
    g "Мы идем по головам, не обращая внимания на тех, кого перемалываем в погоне за своими целями. 
    А иначе просто нельзя: сострадание делает тебя слабым, а слабость для любого руководителя - прямой путь к обрыву со ступенек власти. 
    И чем выше забрался, тем, разумеется, больнее падать." 
    
    g @  smirk "Право сильного двигает современные корпорации вперед, оставляя позади тех, кто не был готов конкурировать. 
    Но это не значит, что добрые люди не нужны. Нет, общество должно на ком-то держаться, пренебрегать чьими-то интересами. 
    Но дело таких людей - знать свое место. Сильные же должны давать им надежды, кормить картинками будущего, которое никогда для них не наступит, и, разумеется, давать второй шанс, который не будет проявлением сострадания, нет." 
    
    g "Он будет светом в конце туннеля для тех, кто по какой-то причине свернул с протоптанной дорожки заурядного будущего. 
    Второй шанс в последний раз разожжет в них чувство благодарности и посеет покорность, открывая возможность управлять им так, 
    как сильному заблагорассудится." 
    
    g @ furious "Ты многое узнал, это правда. Раз за разом закапывая свой нос все глубже в дела корпорации, 
    ты наконец нарыл то, что никому постороннему знать не нужно." 
    
    g @ angry "Мы пытались вернуть тебя на правильный путь: ты стажер - учись, общайся с коллегами, влюбляйся, ходи на встречи и свидания, 
    спокойно создавай игры в конце концов. Но твое любопытство не переставало быть твоим главным двигателем. 
    Тебя предупреждали? {w}Тебе давали шанс? {w}Но ты продолжал следовать призрачным принципам и наконец оказался тут, 
    где оборвется никчемная жизнь пожелавшего тягаться с корпорациями и государством."

    # (рут одиночества) soleCompany = 1 2 3 4 (max 7)     loveLine = 1 2 (max 4)
    if (soleCompany < 5 and loveLine < 3):
        jump fifth_day_root_loneliness
        return

    else:   # soleCompany = 5 6 7    loveLine = 3 4  

    # (рут Элли)  soleCompany = 6 7    loveLine = 3 4  
        if (soleCompany % 7 <= loveLine % 4):
            jump fifth_day_root_love
            return

        # (рут команды - Карэн) soleCompany = 5 6 7    loveLine = 3  
        else:
            jump fifth_day_root_team
            return

    return     