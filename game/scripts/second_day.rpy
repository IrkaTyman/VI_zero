label second_day:
    scene home morning
    with fade

    "{cps=43}Человечество обречено, если в мире прогресса люди должны вставать рано утром… 
    В такие моменты даже мысли о предстоящем дне в компании не греют мою душу. 
    Ничего не поделать, нужно собираться.{/cps}"

    show street
    with fade
    
    "{cps=40}Интересно, что приготовил Кай для меня сегодня. Вряд ли будет так просто, как было вчера. 
    Все-таки им нужно погружать меня в детали разработки, а это темы гораздо более сложные, 
    чем просто описание профессий.{/cps}"
    stop music fadeout 3.0

    show lane morning
    with fade

    "{cps=40}А не Кай ли это? И чего он так подозрительно выглядит? Ну точно он! 
    Стоп, а почему он идет не в сторону офиса? Слишком рано? 
    Возможно, но что может понадобиться рано утром сотруднику богатой корпорации с огромным офисом, где чего только нет.{/cps}"

    menu:
        "Проследить за Каем":
            $ detective += 1
            $ watch_kai = True
            jump track_kai
            return
        "Не следить за Каем":
            $ soleCompany += 1
            jump not_track_kai
    return

label track_kai:
    scene lane morning
    with dissolve

    play music "music/music bad.mp3" fadein fadein volume volume loop

    "{cps=40}Переулок, в который таинственно забрел Кай, совсем не похож на место, 
    где происходит что-то легальное и благонамеренное.{/cps}"

    "{cps=40}Тут что-то не так. Нужно попытаться выяснить, куда он направляется.{/cps}"

    "{cps=40}Черт, надо же было так неудачно встать. Совсем не видно лицо этого незнакомца. И фразы их не разобрать. 
    И все же все это максимально подозрительно. К чему такая скрытность? Никаких ответов…{/cps}"

    "{cps=40}Пора в офис… Не хватало мне опоздать во второй день своей стажировки. 
    А вот как Кай вовремя окажется там, я даже представить не могу…{/cps}"

    scene hall
    with fade

    "{cps=43}Безлюдный холл напоминает, что все ответственные работники уже давно на своих рабочих местах.{/cps}"
    "{cps=43}Так пусто тут… Теперь я действительно начинаю волноваться за свое опоздание.{/cps}"

    jump second_day_contunue
    return

label not_track_kai:
    play music "music/music good.mp3" fadein fadein volume volume loop

    "{cps=43}Не думаю, что дела Кая как-либо меня касаются. В конце концов, имеет же 
    он право вне рабочего времени ходить, куда его заблагорассудится. 
    Я же лучше дойду до кофейни, пока есть время до начала рабочего дня.{/cps}"

    scene coffee house
    with fade
    "{cps=43}Можно один латте, ложка сахара, медовый сироп? Спасибо.{/cps}"

    show lloyd
    with OffsetRightToCenterSide
    l "{cps=43}Здравствуйте! Работящего человека видно сразу, эх! Кстати, Ллойд. 
    Это мое имя. Скажете, что за невнятный тип, а я скажу вам, 
    что я бывший разработчик одной корпорации. Почему бывший? ДА ПОТОМУ ЧТО..{/cps}"
    $ see_lloyd = True
    show lloyd surprise at right
    with move

    show kai at left
    with OffsetLeftToLeftSide
    kai "{cps=43}Привет, стажер. Давненько не виделись. Не обращай внимания на этого сумасшедшего, 
    он давненько в этой кофейне всем настроение портит.{/cps}"
    show kai angry
    kai "{cps=43}Все говорю хозяину заведения, чтобы запретил его пускать. Но тот жуткий либерал, 
    все время твердит про “равенство прав” и прочую лабуду.{/cps}" 
    show kai
    kai "{cps=43}А по мне, так нет смысла возиться с такими психами.{/cps}"

    "{cps=43}Какой-то ты жестокий сегодня. День не задался?{/cps}"
    
    show kai smile
    kai "{cps=43}Да, извини. Как-то само вырвалось. Отдыхать надо почаще, а то работа и работа.{/cps}"


    scene street
    with dissolve

    show kai smile
    with dissolve
    kai "{cps=43}Помнится, я обещал тебе рассказать, как попал в компанию.{/cps}" 
    
    show kai
    kai "{cps=43}Так вот. Я, как и многие, 
    закончил вуз на разработчика ПО, начал бегать по собеседованиям. Провалил одно, второе, третье. 
    “Мы вам перезвоним”. И тишина. В какой-то момент я отчаялся, хотел устраиваться не по профессии,
    когда мне позвонили и сообщили, что берут меня с испытательным сроком в компанию.{/cps}"
    show kai smile_with_disbelief
    kai "{cps=43}Только потом я уже узнал, что похлопотала за меня Карэн. Ей понравилась моя харизма и то, 
    как я готов был стать частью команды. На испытательном все только убедились, 
    что я делаю команду лучше, и взяли меня в штат.{/cps}"

    "{cps=43}А я гляжу, скромности тебе не занимать.{/cps}"

    show kai serious
    kai "{cps=43}Знать себе цену - полезный навык. Запиши в свою книжечку “Правила успешного стажера”.{/cps}"

    "{cps=43}Какие у тебя вообще эмоции от работы в такой крупной компании? Ведь многие годами мечтают 
    попасть в разработку игр, а тебе так повезло, хотя ты вроде и навыками не блистаешь, 
    извини уж за прямоту.{/cps}"

    show kai smile_ce
    kai "{cps=43}Да ладно, чего уж там… Был бы ты не прав, я бы возразил, но я и правда не очень силен 
    в программировании. Но позволь тебе рассказать секрет успешной команды: не так важно, 
    насколько профессиональны члены твоей команды.{/cps}"
    
    show kai serious
    kai "{cps=43}Будь они хоть трижды специалистами мирового уровня, 
    если они плохо взаимодействуют между собой, хорошего продукта не сделать. А все почему? 
    Геймдев - одна из самых зависимых от общего видения команды областей разработки.{/cps}"
    show kai

    "{cps=43}Получается, даже ничего не знающий вполне может попасть в команду?{/cps}"

    show kai serious
    kai "{cps=43}Ну ты уж палку не перегибай, дружище. Разумеется, кроме командной работы важно, что из себя представляет каждый ее член. 
    Поэтому слушай и вникай во все, что я тебе сегодня буду рассказывать.{/cps}"

    scene street
    with dissolve

    scene hall
    with fade

    scene elevator outside
    with dissolve

    show kai
    "{cps=43}Забыл кое-что сделать. Ты давай в лифт, а я следом. Подожди меня за рабочим местом.{/cps}"

    "{cps=43}Ну, как скажешь…{/cps}"

    hide kai
    with OffsetLeftToCenterSide
    
    jump second_day_contunue
    return


label second_day_contunue:
    stop music fadeout fadeout
    pause fadeout

    scene elevator inside
    with dissolve
    
    play music "music/elevator.mp3" fadein fadein volume volume loop

    "{cps=43}Интересно, один лишь Кай в команде такой странный, или другим тоже есть, что скрывать? 
    Нужно постараться аккуратно разузнать что-нибудь у Карэн, при этом не забыть о главной цели 
    - показать себя как перспективного разработчика, чтобы заполучить место в компании.{/cps}"

    "Ну, вперед!    …"

    stop music fadeout fadeout
    pause fadeout
    play music "music/music good.mp3" fadein fadein volume volume loop

    scene office
    with dissolve

    show karen
    with dissolve
    "{cps=43}Доброе утро, Карэн… Я опоздал?{/cps}"

    show karen say
    k "{cps=43}И да, и нет. Технически, ты пришел вовремя, но на будущее: не стоит тянуть до момента, 
    когда до начала дня остаются считанные секунды. Тебе же нужно включить компьютер, 
    устроиться за рабочим местом, наверняка и с коллегами захочешь что-то обсудить. 
    Думаю, ты меня понял.{/cps}"
    show karen smile

    "{cps=43}Да, разумеется. Впредь буду стараться приходить пораньше. Я могу пройти к своему месту?{/cps}"

    show karen say
    k "{cps=43}Проходи, вот только наставника твоего до сих пор нет в отделе. Ты его случайно не встречал?{/cps}"
    show karen

    menu:
        "Сказать правду":
            jump say_true_kai
            $ soleCompany += 1
        "Соврать":
            jump say_lie_kai
            
label say_true_kai:
    "{cps=43}Знаешь, на самом деле мне есть, что сказать. Утром мы…{/cps}"
    jump second_day_office_continue

label say_lie_kai:
    "{cps=43}Да нет, на глаза он мне не попадался, да и сомневаюсь я, что мы могли пересечься по дороге.{/cps}"

    k "{cps=43}Что ж, тогда будем жд…{/cps}"
    jump second_day_office_continue


label second_day_office_continue:
    scene office

    show karen at right
    with move

    show kai smile at left
    with OffsetLeftToLeftSide

    kai "{cps=43}А вот и я! Босс, извиняйте, были неотложные дела. Ты же не станешь делать выговор 
    самому важному сотруднику отдела?{/cps}"

    show karen angry
    k "{cps=43}С чего бы ты…{/cps}"
    show karen

    show kai smile_with_disbelief
    kai "{cps=43}Ну, тогда я побежал. Стажер, давай за мной!{/cps}"

    show karen angry
    k "{cps=43}Но я же еще не успела даже ничего сказать…{/cps}"

    scene office2
    with dissolve

    show kai
    "{cps=43}И чем сегодня будем заниматься? Как вчера, будешь наполнять мою голову терминами?{/cps}"

    kai "{cps=43}Во-первых, без этих самых терминов ты никогда не станешь хоть сколько-нибудь 
    успешным разработчиком. Во-вторых, сегодня я постараюсь немного разнообразить твой день: 
    мы снова немного поговорим о геймдеве в общих чертах, расскажу тебе несколько важных деталей, 
    затем ты поработаешь над подготовленным мною заданием, а еще мы сходим в кафе на последнем этаже.{/cps}"

    "{cps=43}Ого, довольно насыщенное расписание. Мы точно все успеем?{/cps}"

    show kai serious
    kai "{cps=43}Успеем, если не будем сидеть и ничего не делать, как сейчас. 
    Кстати, еще небольшой сюрприз тебя ждет в конце дня. Так что давай начинать.{/cps}"
    show kai

    "{cps=43}Ты меня заинтриговал, надеюсь сюрприз - не очередная твоя дурацкая шутка. Но начать и правда стоит.{/cps}"

    kai "{cps=43}Не знаю, обрадую тебя или огорчу, но мы с Карэн побеседовали и решили попробовать 
    обучить тебя основам программирования игр, раз уж в университете тебе довелось писать алгоритмы 
    и их реализацию на разных языках программирования. Так ведь?{/cps}"

    "{cps=43}Ну, не на разных, а только на одном. Но в целом все так.{/cps}"

    show kai smile
    kai "{cps=43}Значит, ты не против постижения программистской стороны геймдева?{/cps}"
    show kai

    "{cps=43}Я бы сказал, что очень даже за. Честно говоря, именно этого я и хотел, когда впервые ехал 
    в этот офис. Правда меня пугало отсутствие опыта в создании игр.{/cps}"

    kai "{cps=43}Вот с опыта давай и начнем. Допустим, ты новичок в мире игр, 
    но у тебя огромное желание попасть в индустрию и куча свободного времени, 
    которое ты готов на это потратить. Каков твой план?{/cps}"

    "{cps=43}Ну, наверное начну читать книги по созданию игр и смотреть видео про это.{/cps}"

    show kai serious
    "{cps=43}И это все замечательно, но про самое главное ты забыл. Ты должен понять, какие игры хочешь создавать.
    Конечно, ты в начале пути и сам еще не знаешь многого о себе, да и по мере развития твои вкусы могут меняться. 
    Но без хотя бы отдаленного представления о том, как должно в итоге выглядеть твое детище, 
    ты не сможешь работать. А даже если и сможешь, то это будет неэффективно.{/cps}"

    kai "{cps=43}И уж конечно тебя не возьмут ни в какую команду, потому что, как я уже говорил, 
    в команде должна быть химия, это маленькая творческая лаборатория, а ты заявляешься в нее без знания, 
    что ты “собрался синтезировать”.{/cps}"
    show kai

    "{cps=43}То есть я должен знать, о чем будет моя игра?{/cps}"

    kai "{cps=43}Отчасти это так, но я имел ввиду не это. Как минимум, ты должен понимать, 
    на каких платформах выйдет игра, и какого жанра она будет. Предвидя твой вопрос, как платформа 
    вообще влияет на игру, отвечу: не представляешь, насколько сильно. К примеру, 
    от величины экрана меняется размер того, что ты сможешь уместить на нем.{/cps}"

    show kai serious
    kai "{cps=43}Но тебя больше должно беспокоить не это. Ты - программист, а значит тебе нужно знать, 
    на каком языке ты будешь писать, а тут платформа оказывает непосредственное влияние на твой выбор.{/cps}"
    show kai

    "{cps=43}Хорошо, тогда расскажи мне о связи языков с платформой.{/cps}"

    show kai smile_with_disbelief
    kai "{cps=43}Есть ряд проверенных временем языков. Конечно, за последние двадцать лет придумали много новых, 
    во внутреннем устройстве которых разберется только высококлассный инженер ПО, 
    но в качестве обучения расскажу тебе о классических языках.{/cps}" 
    
    show kai serious
    kai "{cps=43}К примеру, для быстродействия крупных 
    десктопных проектов раньше выбирали такой язык, как C++. Со временем новички вытесняли его тем, 
    что обеспечили более аккуратную работу с памятью. Но он все равно прожил очень долго и использовался 
    в огромном числе проектов. Более аккуратен в этом плане, однако от этого более медлительный - C#. 
    Он использовался в популярных движках, на которых делали игры на ПК и консоли.{/cps}"
    
    show kai
    kai "{cps=43}Размеры проектов на этом языке уже могли быть различны: возможно было довольно удобно создать 
    и что-то небольшое, и что-то глобальное. В один момент в моду вошло делать кроссплатформенные игры, 
    тогда на помощь пришел Java со своей виртуальной машиной.{/cps}"

    "{cps=43}А как на счет онлайн игр?"

    kai "{cps=43}Когда скорость соединения наконец стала адекватной, такие проекты заполонили рынок. 
    Многие из них использовали JavaScript. И нет, он не связан с Java!{/cps}"

    "{cps=43}А был ли какой-то язык, который позволял быстро и просто создать что-то не требовательное и, 
    может, не очень производительное?{/cps}"

    show kai smile_with_disbelief
    kai "{cps=43}Не просто был, он и сейчас есть. Python. За счет своей простоты и любовь со стороны сообщества, 
    он постоянно имел поддержку и так дожил до наших дней. 
    Так что, если вдруг захочешь что-то написать дома, можешь попробовать его.{/cps}"
    show kai

    "{cps=43}Ну хорошо. Я выбрал платформу, жанр, язык программирования, потратил время на его изучение, 
    а также следил за всей индустрией и играл во многие новые и старые игры. 
    Что мне делать дальше, как попасть в команду?{/cps}"

    show kai smile
    kai "{cps=43}Во-первых, хочу похвалить тебя. Ты очень точно заметил, что важно оставаться в курсе 
    последних новостей в мире игр, чтобы всегда пользоваться последними технологиями и создавать 
    актуальный продукт.{/cps}" 

    show kai 
    kai "{cps=43}А как сам думаешь, что тебе нужно, чтобы твою кандидатуру рассмотрела компания?{/cps}"

    show kai serious
    kai "{cps=43}Даже не пытайся говорить “попасть на стажировку”. Это тебя заметили, но некоторым приходится 
    стараться и добиваться рассмотрения своего портфолио. Собственно, его тебе и нужно подготовить, 
    чтобы попасть в компанию.{/cps}"
    show kai

    "{cps=43}Из чего оно должно состоять?{/cps}"

    kai "{cps=43}Из нескольких твоих игр. Обычно это профиль на хостинге проектов, 
    где работодатель сможет посмотреть, когда, сколько и что ты писал. 
    Поэтому важно все красиво и качественно оформить, скрыть тренировочные проекты, 
    постараться и придумать что-то действительно стоящее, ну и надеяться, что твое портфолио оценят.{/cps}" 

    show kai serious
    kai "{cps=43}Кстати, еще тебе понадобится резюме. Множество шаблонов ты можешь найти в интернете, 
    но сейчас я хочу дать тебе небольшое задание: попробуй заполнить пропуски в этом резюме, 
    ориентируясь на свой опыт и знания.{/cps}"
    show kai

    jump resumeGame_label
    return

label resumeGame_label:
    scene office2
    show kai
    jump resumeGame
    return


label second_day_contunue_after_game:
    show office2
    with dissolve

    show kai
    with dissolve

    "{cps=43}Ну, как я справился?{/cps}"

    if developer >= 3:
        show kai smile
        kai "{cps=43}Очень неплохо, получилось что-то действительно похожее на настоящее резюме, 
        теперь ты хотя бы представляешь, как оно должно выглядеть. На этом пока остановимся, 
        нам пора на последний этаж здания в кафе.{/cps}"

        "{cps=43}Ну, тогда идем.{/cps}"
    else:
        show kai serious

        kai "{cps=43}Честно говоря, ты ответил не совсем правильно в некоторых местах, 
        но так как я не давал тебе теории по этой теме, ругать не стану. 
        Просто как-нибудь дома потрать немного времени на это и попробуй понять, 
        где и почему допустил ошибки. Идет?{/cps}"

        "{cps=43}Ладно, постараюсь разобраться…{/cps}"

        show kai 
        kai "{cps=43}Эй, а ну не вешать нос! Ты же не проект запорол, а просто не очень справился 
        с простеньким заданием. Давай сходим на обед и немного отвлечемся от работы.{/cps}"

        "{cps=43}Ну, тогда идем.{/cps}"

    jump second_day_elevator
    return