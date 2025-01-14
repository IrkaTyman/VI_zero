label first_day_morning:
    play music "music/music good.mp3" fadein fadein volume volume loop
    scene street
    with fade

    """{cps=43}Такое здание ни с чем не перепутаешь. Значит, мне сюда…{/cps}"""

    show kai at center
    with OffsetLeftToCenterSide

    kai "Утречка, всем своим видом ты даешь понять, что спрашивать нет смысла, но все же: это ты наш стажер?"

    "Здравствуйте… А что, правда так заметно?"

    kai "{cps=40}Правда. Ты же бледный весь и словно готов в любую секунду убежать отсюда. Тебе не стоит так волноваться, может внешне корпорации и выглядят устрашающе, но люди внутри куда более доброжелательны и дружелюбны, чем всем кажется.{/cps}"
    kai "{cps=40}Я, конечно, могу стоять тут с тобой и разговаривать хоть весь день,но влетит от тимлида и тебе, и мне, так что давай не будем испытывать терпение Карэн и поспешим в офис.{/cps}"

    scene hall
    with fade

    show kai
    "Тимлид - это наш руководитель? И ее зовут Карэн?"
    kai "Именно. Тимлид - это ответственный за работу одной из сотни групп нашей огромной компании. Наш с тобой начальник - Карэн. Со всеми самыми важными вопросами тебе лучше обращаться прямо к ней."
    "Спасибо, буду знать. Кстати, я забыл спросить ваше имя."

    scene elevator outside
    with fade

    show kai
    kai "Во-первых, меня зовут Кай. Во-вторых, давай уже “на ты”. Нам с тобой над одними задачами вместе работать, да и в команде нашей принято общаться без всяких “вы”. К слову, твое имя я тоже еще не знаю."
    "Меня зовут Макс"
    kai "Ну, [nameM], добро пожаловать в компанию!"

    scene elevator inside
    with fade
    stop music fadeout fadeout
    pause fadeout
    play music "music/elevator.mp3" fadein fadein volume volume loop

    show kai smile 
    with OffsetRightToCenterSide

    kai "Наш офис на 102-ом этаже, так что несколько минут каждого своего дня нам приходится тратить на поездку в тесном лифте."
    kai "Но зато, по слухам, иногда тут можно столкнуться даже с {i}высочайшим руководством{/i} компании. Мне пока не удавалось, но я и работаю тут всего ничего."
    kai "Кстати, обязательно нужно рассказать тебе, как я попал в команду. Но это довольно долгая история, так что как-нибудь в другой раз."

    "Кай, есть еще что-то, что я должен знать перед тем, как зайти в наш отдел?"

    show kai serious
    kai "Дай-ка подумать… Ну, кабинет Карэн в конце коридора. А все остальное можно узнать уже там."
    show kai smile_wide_ce
    kai "Я шучу, конечно. Если вдруг что-то понадобится, лучше сначала спроси меня. Наш тимлид - очень занятая и ответственная девушка, а потому лучше не беспокоить ее без повода."
    show kai smile

    "А меня будут тестировать по уже имеющимся знаниям о геймдеве? Если честно, я не так уж много всего знаю…"

    kai "Не переживай, если что-то и будут спрашивать, то по уже рассказанному тебе за время стажировки, ничего такого, что ты бы не услышал или не увидел в стенах офиса. В конце концов, мы все тут понимаем, что ты только закончил первый курс."
    "Спасибо, я переживаю уже гораздо меньше."
    kai "Для этого я и курирую тебя. А теперь нам пора в отдел."
    stop music fadeout fadeout
    pause fadeout

    scene office
    with fade
    play music "music/music good.mp3" fadein fadein volume volume loop
    play sound "music/keyboard.mp3" fadein fadein volume volume loop
    
    show kai at left
    with OffsetLeftToLeftSide
    pause 0.5

    show karen at right
    with OffsetRightToRightSide
    
    k "Кай, [nameM], я уже собиралась начать ваши поиски. В самом деле, где вы пропадали?"
    kai "Ну Карэн, ты же знаешь, сколько всего нужно спросить новичку у опытного наставника"
    "{cps=50}Но я не спраш…{/cps}{nw}"
    show kai smile 

    kai "Да-да, ты не знал много всего о работе в крупной компании, но я всегда рад прийти на помощь."
    "Ага, спасибо большое…"
    k "Ладно, сейчас главное - не продолжать тратить время попусту. Кай - на свое рабочее место, я поговорю с ним и отправлю его к тебе."
    show kai smile_wide_ce 
    kai "Слушаюсь!"
    hide kai
    with OffsetRightToRightSide
    
    show karen at center
    with move

    k "Я Карэн, руководитель этого отдела разработки. Как ты уже знаешь, тебя отправили к нам на стажировку. Ты получишь начальные знания о работе разработчиком игр, а после мы решим, что с тобой делать."
    show karen smile
    k "Этот парень - твой наставник. Пусть он сам только-только стал частью коллектива, да и шуточки его могут порой раздражать, но у него здорово получается налаживать взаимодействие между людьми, потому он должен стать подходящим человеком, чтобы ввести тебя в курс корпоративной жизни."
    show karen
    k "А теперь отправляйся на рабочее место и впитывай так много информации, как только сможешь."

    scene office2
    with fade

    show kai
    "Ты, кажется, говорил что-то про дружелюбную атмосферу. Как-то мне не показалось, что Карэн к нам дружелюбна."
    show kai serious
    kai "Зря ты это. Может с виду она требовательна и слегка груба, но на самом деле на ее плечах лежит огромная ответственность, которую она предпочитает не перекладывать на других. Да и характер у Карэн очень даже приятный, просто нужно узнать ее получше и заслужить ее уважение."
    "Руководители… Никогда с ними не бывает просто. Ладно Кай, давай уже начнем рабочий день, а то уже и полдень наступил, а мы ни строчки кода и не написали."
    show kai smile
    kai "И не напишем. Ты то думал, придешь и сразу игры кодить? Спешишь, друг, очень спешишь. Сегодня твой первый день в компании, а потому говорить будем только об основах геймдева. Кстати, ты вообще знаешь, что это такое?"
    "Ну ты уж совсем за дурака меня не принимай… Геймдев переводится как"

    menu:
        "Тестирование игр":
            kai "Ошибочка."
            kai "Геймдев - это разработка игр. Ничего страшного, не все знают английский. Хотя, честно тебе скажу, без него в этой отрасли никуда. Да ты и сам наверное знаешь, что вся документация языков программирования и игровых движков написана на нем."

        "Продажа игр":
            kai "Ошибочка."
            kai "Геймдев - это разработка игр. Ничего страшного, не все знают английский. Хотя, честно тебе скажу, без него в этой отрасли никуда. Да ты и сам наверное знаешь, что вся документация языков программирования и игровых движков написана на нем."
        
        "Разработка игр":
            kai "Верно! А я уж думал начать тебя недооценивать. Просто знал или перевел с английского?"
            "Знал, но и с английского могу некоторые термины переводить. Я понимаю, что без знания языка в программировании трудно. Все-таки за год учебы в университете мне довелось и документацию языков программирования читать, и гайды на английском смотреть."

    kai "Думаю, прежде всего нужно рассказать тебе о профессиях внутри нашей, да и внутри других команд разработки тоже. Что ты уже знаешь по этой теме?"
    "Я знаю, что разработчик игр - обобщенное название всех профессий этой отрасли. Я бы хотел услышать, какие имеются в вашей компании."
    kai "Хороший вопрос. Пусть тебя и взяли на стажировку как разработчика игр, рано или поздно тебе придется выбрать более узкое направление, а для этого тебе нужно хотя бы отдаленно представлять, чем занимаются те или иные члены команды разработки."
    show kai smile_wide_ce
    kai "Тебе повезло, что ты попал в такую огромную компанию, как наша. У нас много отделов, занимающихся кардинально разными проектами. И в каждом отделе востребованы разные роли."
    show kai smile
    kai "К примеру, уже несколько десятилетий игроки любят онлайн проекты и проводят в них очень много времени. А ты знаешь, какие профессии наиболее важны для организации правильного взаимодействия сотен игроков со всего мира?"

    menu:
        "Программист":
            kai "Действительно, для онлайн игр важна согласованная работа программиста, занимающегося сетевым кодом, и разработчика БД, тогда данные будут корректно поступать от игроков к серверу, а вся новая информация будет вовремя записываться в базу данных."
        "Разработчик баз данных":
            kai "Действительно, для онлайн игр важна согласованная работа программиста, занимающегося сетевым кодом, и разработчика БД, тогда данные будут корректно поступать от игроков к серверу, а вся новая информация будет вовремя записываться в базу данных."
        "Data-scientist":
            show kai
            kai "Не совсем. Для онлайн игр важна согласованная работа программиста, занимающегося сетевым кодом, и разработчика БД, тогда данные будут корректно поступать от игроков к серверу, а вся новая информация будет вовремя записываться в базу данных."
    
    "Слушай, Кай, a тимлид - это тоже профессия?"
    kai "Не совсем. Тимлид - это должность, а профессия руководителя проекта называется project-менеджер. Это очень важная для любой компании должность, поскольку работа такого профессионала сочетает в себе построение коммуникаций между другими членами команды и непосредственное производство продукта."
    kai "Если хочешь стать project-менеджером, тебе нужно разбираться в вопросах стоимости и финансирования, качества, рисков, безопасности и еще сотни важных сторон разработки любого продукта."
    "Звучит устрашающе. Я правильно понимаю, что у нашей команды project-менеджер это Карэн?"
    show kai smile
    kai "Угадал. Именно поэтому я говорил тебе об огромной ответственности на ее плечах"
    "Кажется, я начинаю ее понимать…"
    kai "{cps=60}Одна из самых интересных, по моему мнению, профессий в геймдеве - это геймдизайнер.{/cps}"
    "О, а с этой профессией я знаком! Я немного интересуюсь геймдизайном. Не скажу, что очень много знаю, но все же эта область геймдева наиболее мне знакома."
    show kai smile_wide_ce
    kai "А ты нравишься мне все больше и больше, парень! Я тоже увлекаюсь этим направлением, хотя и работаю тестировщиком. Это еще одна важная профессия в разработке игр."
    show kai smile
    kai "Наверняка ты сталкивался с неработающими и забагованными играми. QA-инженеры, так еще называют тестировщиков, занимаются поиском дефектов в продукте и выявлением ошибок на всех этапах разработки."
    "Терпеть не могу, когда во время игры что-то перестает работать в самый неподходящий момент. Выходит у тебя тоже довольно важная роль в команде, несмотря на то, что ты тоже новичок."
    show kai eyes_side
    kai "Эй! И никакой я не новичок."
    show kai
    kai "По крайней мере, я полноценный член команды, а не просто стажер. И вообще, я так тебе скажу: в создании игр нет профессий, чья работа не была бы важна. К примеру, долгое время нарративный дизайн не выделяли в отдельное направление разработки."
    kai "Но с годами компании осознали, как важно иметь человека, который будет качественно интегрировать сюжет и геймплей и продумывать, как игровые механики будут раскрывать пользователю мир игры."
    "Звучит как профессия, которая подойдет очень креативному человеку, по настоящему любящему игры и часто играющему в них."
    show kai smile
    kai "Ты прав, нарративный дизайнер должен много, а главное вдумчиво проходить проекты различных жанров и сеттингов, чтобы расширять границы своей фантазии и находить все более оригинальные способы раскрыть мир игры через различные ее элементы."
    "Если я правильно понял, то нарративный дизайнер больше отвечает за осмысленность механик и геймплей. А чем занимаются сценаристы?"
    kai "Сценаристы в первую очередь создают тот нарратив, который позже будет встраиваться в игру дизайнерами. Любая история должна иметь какой-то смысл, какой-то контекст, поэтому даже в простеньких играх стараются делать хотя бы незатейливый сюжет."
    kai "Обычно сценаристы тесно работают с геймдизайнерами и нарративщиками, потому что мало написать интересный, захватывающий сюжет, что само собой является работой сценариста, нужно еще и умело связать его со всеми элементами игрового мира, сделать так, чтобы все в истории подчинялось одной логике."
    kai "Любой сценарист должен быть трудолюбив и любознателен, и только тогда из-под его пера будут выходить работы, по-настоящему погружающие игрока в созданный мир."
    "Мне показалось, что это самая ответственная профессия после project-менеджера. Так ли это, Кай?"
    kai "Не берусь судить, приятель. Тяжело сравнивать между собой настолько разные по своим обязанностям профессии. Зато есть ряд профессий, чью работу пользователь обязательно увидит, когда будет проходить игру. Как ты думаешь, кто не входит в этот ряд?"

    menu:
        "Художник":
            show kai
            kai "Вовсе нет"
            "Правда? Но кто же тогда?"
            show kai smile
            kai "ML-специалист, но давай расскажу о каждой профессии из этого списка"
        "VFX-дизайнер":
            show kai
            kai "Вовсе нет"
            "Правда? Но кто же тогда?"
            show kai smile
            kai "ML-специалист, но давай расскажу о каждой профессии из этого списка"
        "Риггер":
            show kai
            kai "Вовсе нет"
            "Правда? Но кто же тогда?"
            show kai smile
            kai "ML-специалист, но давай расскажу о каждой профессии из этого списка"
        "ML-специалист":
            kai "Верно. Но я все же расскажу про каждую их этих профессий."
            "Ладно, давай…"
    kai "Начну с ML-специалиста. Это человек, который занимается тренировкой и поддержкой моделей машинного обучения. Не скажу, что таких специалистов нет в нашей компании. В основном они отвечают за реалистичное поведение внутриигровых персонажей."
    show kai smile_wide_ce
    kai "Благодаря им герои не врезаются в стены, а враги стреляют в цель и умеют кооперироваться. Ну, по крайней мере так должно быть в качественном проекте, прошедшем грамотное тестирование."
    show kai smile
    "Меня всегда удивляло, как игра может противостоять игроку. Теперь понятно, кто за это отвечает. И все же, что на счет профессий, чью работу любой игрок видит, проходя игру?"
    kai "Вот мы и подошли к самым красочным, самым творческим членам нашей компании. Конечно, у каждого проекта есть целая команда различных художников. Но разделяют в основном текстурных художников, занимающихся доработкой 3D моделей до необходимого для игры вида, художников по игровому арту, которые рисуют графику и оформляют игру, аниматоров, 3D-моделлеров, и еще много-много профессий, отвечающих за картинку, которую будет видеть игрок."
    kai "Но я также упомянул еще VFX-дизайнера, который создает визуальные эффекты, которые делают проект намного более эффектным, и 3D риггера, который выполняет роль связного между создателями моделей персонажей и аниматорами."
    "Ты забыл еще одну профессию, чья работа сразу видна игроку."
    show kai smile_ce
    kai "Да, и про кого же ты?"
    show kai smile
    "Ну, саму профессию не могу назвать, но это кто-то, ответственный за звук."
    show kai eyes_side
    kai "Точно! И как я только мог забыть…"
    show kai
    kai "Основная ответственность за звук в игре ложится на плечи звукорежиссера. Именно он отвечает за качество звукового ряда, работает над созданием правильных звуковых образов. С виду, может, и не заметно, насколько глубоко связана музыка и персонажи, но настоящий профессионал очень сильно помогает раскрыть героев и мир игры с помощью звукоряда."
    "Мы так много говорили про различные творческие профессии в геймдеве. Но ведь никакую игру не создать без способного программиста, не так ли?"
    show kai smile
    kai "Тут с тобой тяжело не согласиться. Ведущий программист - одна из ключевых должностей в команде. Эти люди отвечают за реализацию всей технической части проекта, всех механик и движка. Хороший программист должен не только знать несколько языков программирования, поскольку чем более сложная и ресурсоемкая задача, тем более низкоуровневым должен быть язык, о чем мы еще поговорим в какой-нибудь из дней твоей стажировки."
    kai "Но также важны его знания в области математики и физики, поскольку оптимизация кода требует глубокое понимание всего, что происходит внутри игры."
    "Фух… сколько же всего ты мне рассказал. Кажется, ты настолько увлекся разговором, что забыл про обед. Смотри, сколько уже времени."
    show kai
    kai "Обед… А ты прав… Ну ничего, мне еще столькому нужно тебя научить, тут некогда расслабляться."

    show kai smile at left
    with move

    show karen smile at right
    with OffsetRightToRightSide
    "Кай, мне кажется, что парень достаточно выслушал от тебя за сегодня. Может, отпустим его домой, а свой рассказ о всех прелестях нашей работы ты продолжишь завтра?"
    show kai sad
    kai "Как скажешь… Значит, до завтра, [nameM]. Буду ждать тебя, не опаздывай!"
    hide kai
    with OffsetLeftToLeftSide

    show karen at center
    with move
    k "Но перед тем, как ты уйдешь, я бы хотела немного побеседовать с тобой о том, что ты за сегодня успел усвоить. Не волнуйся, это не зачет и не контрольная, просто небольшой опрос для того, чтобы я понимала, как идет твое обучение."
    "Хорошо..."

    stop sound fadeout fadeout

    jump first_day_survey
    return