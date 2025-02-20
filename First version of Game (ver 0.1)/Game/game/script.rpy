﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define u = Character('Дядя',color="#107dd7", image="uncle")
define p = Character('Саша', color="#e39319")
define f = Character('Папа', color="#e3aa0d")
define m = Character('Мама', color="#e3580d")
define n = Character('Серега', color="#435bd0")
define mih = Character('Миша', color="#0c8251")
define krist = Character('Кристина', color="#149952")
# image uncle_happy: 
#     "uncle happy.png" 
#     zoom 0.8
# image uncle: 
#     "uncle.png" 
#     zoom 0.8
# image uncle_curious:
#     "uncle curious.png"
#     zoom 0.8
# init:
#     $ right = Position(xalign=0.8, yalign = 1.99999999)
# Игра начинается здесь:
label start:
    scene street with fade
    "WHO" "Саша сдал последний экзамен и больше не хотел думать об учебе. 
    Большую часть своего последнего школьного лета он проводил, как хотел." 
    "И в один момент в его голове засела мысль о поступлении. 
    Не зная куда поступать, Саша решает обратиться к своему дяде, работнику крупной IT компании, за помощью"
    """
    Легкий солнечный денек, об учебе не было и мысли.

    Из дел остались только не лёжаный диван и недосмотреный сон.

    Впереди последнее школьное лето.
    """
    with fade
    """
    Кхм.. О чем это я?

    Ах да, все лето проходило беззаботно, до того момента, пока меня не окутала мысль о моем скором поступлении.

    С этим были небольшие проблемы, ведь я совсем не имел понятия, куда себя определить и хочу ли я этого.

    Может быть вовсе пойти работать?    
    """
    with fade
    """
    Несколько дней в блужданиях от выбора к выбору ни к чему не привели.

    Я отправился за советом к своему многоуважаемому дядьке Дмитрию Владимировичу.

    Он работал в крупной IT компании, о которой я почти ничего не знал, кроме того, что она крупная.
    
    """


    

label uncle_house:
    scene house with fade
    p """
    Я подошел к дому своего дяди.

    Внутри по видимому вообще никого не было, но я все равно решительно ткнул на кнопку звонка.

    Динь-дон. Динь-дон
    """
menu ring_menu:
    "Что мне делать ?"

    "Пытаться звонить дальше":
        "Никто не отвечает"
        jump ring_menu
    
    "Отойти от звонка":
        p "Похоже его все-таки нет дома"
        p "Придется наведаться к нему в офис той самой IT компании"
label office_introduction:
    scene lift with fade
    show uncle at right:
        yalign -0.5
    p "Дядька встретил меня у лифта, крепко пожал руку и с веселой усмешкой поприветствовал меня."
    scene itinside with fade
    show uncle at right with moveinleft:
        yalign -0.5
    p "Я уже бывал тут, когда был еще ребенком. С тех пор тут мало что изменилось"
    p "Он провел мне небольшую экскурсию, пока мы шли до его кабинета"


label office_talk:
    scene office
    show uncle at left with moveinleft:
        yalign -0.5
        xzoom -1.0
    p "Я хотел у тебя кое что спросить."
    p "Скоро мне нужно будет поступать, но я еще даже не определился с направлением."
    p "Не говоря уже о выборе учебного заведения.Не мог бы ты что нибудь подсказать?"
    
    u "А какие экзамены ты осилил ?"
    
    p "Информатика, профильная математика"
    u @happy "Я думал тебе больше нравится ИЗО"
    p "Ха-ха"
    p "{i}Он никогда не терял возможности сострить{/i}"
    u "Ну ладно, шутки шутками, а дело серьезное."
    u "Ничего великого я тебе не поведаю, но могу рассказать, как я поступал и куда"
    p "{i}Давно я не слушал историй от дяди{/i}"
    u """ 
    Как только появились компьютеры, да машины всякие вычислительные, так меня и потянуло на них.

    Понятного было мало, но тяга к неизведанному и неизвестному пересилила мои страхи по этому поводу.

    А раз было такое рвение и интерес, я думаю, что ты уже догадываешься, что я сделал.
    """
    p "Ага..."
    u "Я выучился на бухгалтера"
    p "Это объясняет твое нынешнее положение"
    u """
    На самом деле не самый очевидный поступок, но можно сказать, что из-за этого я здесь. Ты совершенно прав.

    В любом случае это положило начало моему продвижению в этой сфере. Я на голову обходил всех своих одногруппников, потому что не первый раз встречался с этим куском металла.
    
    Так я понял, что из каждого дела можно извлечь пользу, и что это может помочь в будущем.
    
    Так что не бойся ошибиться в своем выборе. В любом случае ты чему то научишься и многое узнаешь 
    """
    u @happy "Например то, что тебе не нравится специальность, которую ты выбрал"
    u "Я со второго раза понял, чем я действительно хочу заниматься и это совсем не страшно: сделать ошибку в выборе"
    u "А захочешь - перепоступишь"
    "~Странное чувство, будто меня только что прочитали~"
    u "А по поводу твоего выбора сейчас, тебе же все таки нравится программирование. Я прав?"
    p "Да, но я не уверен"
    u "В любом случае тебе стоит попробовать"
    "~Эти слова еще больше вдохновили меня. Такое теплое чувство~"
    p "Так, и какие направления ты бы посоветовал?"
    "~Собственно с этим вопросом я и пришел~"
    u "Сам я поступал в Урфу у нас в городе, а учился вон за тем домом"
    "Тут он показал в сторону многоэтажек"
    u "В Урфу вообще много специальностей с твоим набором экзаменов, и тем более там будут рады таким заинтересованным молодым людям"
    "Его оборвал телефонный звонок"
    u curious"Да.. Понял... Сделаю, да"
    "Повесив трубку, он вдруг забегал глазами"
    u -curious "Очень рад был тебя увидеть, Саша. Я рассказал тебе все, что знал, иди с миром"
    u "У меня появилось довольно срочное дело, так что вынужден с тобой проститься. Был рад увидеться"
    hide uncle with moveoutleft
    p "Я тоже был рад тебя увидеть. Спасибо, что нашел минутку для меня"
    p "Странный он какой-то сегодня"
    "Вместе с ним и этими мыслями я вышел из его офиса и направился к лифту"
    scene lift
    p """
    Мне стоит хорошенько подумать обо всем этом

    Я уже хотя бы знаю в какую сторону начинать двигаться

    Начинать свой путь в неизведанное.
    """
label DayAfterOffice:
    scene room
    """
    Что ж, сегодня же я залез в интернет, чтобы скорее определиться с направлением

    Заглянув на сайт городского университета я посмотрел и оценил больше 20-ти направлений, и все они были действительно интересными
    
    Выбор был не из легких, в каждом было то, что меня влекло

    Баллов у меня достаточно, так что сразу определился, что это будет развитое и популярное направление

    Спустя пару дней серфинга, я всё выяснил. Самым популярным направлением было Программная инженерия

    Честно, сам сначала не понимал, чего там такое, так что я связался со старостой этого направления, который в подробностях рассказал мне о нем.
    
    Завлекает не столько перспектива, сколько учебный процесс.

    Чем больше я узнавал подробностей, тем больше был мой интерес.

    Все таки где-то здесь есть подвох

    И он не заставил себя долго ждать…

    ПОДАЧА ДОКУМЕНТОВ

    А также встреча с приемной комиссией.

    Эти дела с самого начала не внушали доверия, но, как оказалось, без этого никак.

    Значит следующий мой шаг был ознакомление с процессом подачи документов

    Это можно сделать 2-мя способами: Очно или через сайт Университета

    Посоветовавшись со своим “другом” старостой, я понял, что лучше ехать в город, где находится этот университет

    По его словам: “... Когда начинается вся эта заварушка с подачей документов, куча ребят из других городов не могут сами присутствовать на подаче. От того сервис грузит по самые не балуйся. Потом сиди и думай, когда тебя обработают и зачислят”

    Не надо мне такого. Приеду и точно подам документы, точно зачислюсь, точно стану студентом Программной инженерии.
    
    Такие мысли! я аж воодушевился. Мне бы речи писать
    
    Такс, теперь стоит разузнать, какие именно документы нужно подавать
    """
label Train_station:
    scene station
    """
    Собрав все документы и купив билет на ПОЕЗД, спустя 2 дня я отправился прямиком на вокзал. Все таки взрослый мальчик уже, поеду один

    Это был обычный железнодорожный вокзал. Из репродукторов доносились невнятные рейсы, со скрежетом но я их различал.

    Перед отъездом захотелось есть. Вокзальная кухня - чистая лотерея. Но я довольно азартный человек.

    Еще не до конца разделавшись с жирным, машино-масляным беляшом, я услышал знакомые слова, знакомые цифры.

    """
    play sound "trainarrive.mp3"
    "Радио" "Уважаемые пассажиры, начинается посадка на поезд номер 312, просьба пройти на посадку, платформа №14…"
    """
    ~О, мой поезд~
    
    Я решил не торопиться, ведь посадка только началась…
    """
    with fade 
    scene black
    "{i}Спустя 20 минут{/i}"
    with fade
    scene train
    """
    Отдав беляш голубям, разрывая легкие глубоким постбеговым дыханием, я все же успел на посадку
    
    Этот поезд напоминал электричку, особенно этот вагон. Тут были только сидячие места. Я взял самые дешевые билеты, ехать все равно не очень долго.
    
    Eще мгновение – и мы тронулись.
    """    
    with fade
    play sound "trainarrive.mp3" #ЗАМЕНИТЬ
    """По пути я про себя перечислил все вещи и документы, которые взял с собой.

    Не забыл ли я чего. 

    ~Главное, что голову не забыл, а с остальным разберусь~
    """
label Ekaterinburg_after_train:
    with fade
    scene street2
    """
    Спустя пару часов стука поездных колес, моему взору представился совершенно новый для меня город.
    
    Я с нетерпением ждал этой встречи, хотя этот город, кажется, ничем не отличался от многих других. Но в этот момент я чувствовал себя особенным

    Это довольно большой город, его даже называют 3-й столицей России.

    Общественный транспорт – удача моей судьбы. Пробиваю по картам местные автобусы, иду на нужную остановку и вот он, мой транспорт до университета.

    На проезд мне пришлось выложить в полтора раза больше, чем у нас. Грабеж, но это не испортило моего настроения.

    Погода сегодня солнечная, а значит, меня ждет успех. Не то чтобы я суеверный, у меня предчувствие.

    Меня очень любят называть оптимистом головного мозга. Почему бы и нет.

    Улицы проносились мимо и размазывались лучами. Легкий прищур не сходил с моего лица, будто песок с ветром пролетел по всему автобусу.

    Очень хотелось побыстрее добраться. Чем дольше я сидел, тем жарче становилось в салоне.

    Несмотря на лето, многие люди торопились и ходили со скоростью света.

    Так выглядел большой город.
    """
label University_first_time:
    with fade
    scene uni
    """    
    Наконец сойдя на своей остановке, я увидел здание института. Это был большой блок бетона, замешанного с архитектурной идеей.
    
    Я шагнул прямиком в главные двери. Завораживающее ощущение.
    """
    with fade
    scene uni inside
    """
    Вокруг было много поступающих и помогающих поступать.

    При входе меня поприветствовали и подсказали куда пройти, чтобы найти нужный мне факультет.

    ~Интересное местечко~

    Я сел за стол переговоров. Мне почти навязали необходимость этого факультета, рассказали о его приоритетности и востребованности.

    Мне была не нужна вся эта пустая болтовня. Я знаю зачем сюда пришел.

    Но ради приличия я дослушал их до конца.
    """
    p "Спасибо за информативный рассказ, но я уже знаю куда пойду."
    "Я живо заполнил и подписал пару бланков. Мне сказали пройти в один из кабинетов этого огромного здания, куда я тут же направился."
    scene auditory2
    """
    Обилие студентов навеяли мысли о том, что любой из них может стать моим лучшим другом, а может, мы никогда больше и не встретимся.

    Забуксовав в своих мыслях, я чуть не пропустил кабинет.

    По-правде говоря, сделать это было сложно. Пропустить свой кабинет.

    чередь в него тянулась от самого поворота с лестницы, а это, между прочим, около 30-ти метров абитуриентов, разбросанных по всему коридору.

    Голодные до знаний, а то и просто голодные абитуриенты входили в кабинет соответственно очереди. Пару часов – и очередь дошла до меня.

    За это время почти не постарел, смог познакомиться с парой ребят гуманитарной специальности с надеждой, что еще когда-нибудь встретимся.

    Зайдя в кабинет и посидев там 5 минут, 4:50 из которых я слушал то, что прочитал накануне на сайте университета, я подписал пару бумажек и тут же покинул его.
    
    ~И ради этого я сидел тут несколько часов?~
    """
    with fade
    scene uni
    "Наконец я покинул здание."
    "~Документы я подал. Осталось только ждать зачисления…~"
label admission:
    with fade
    scene room
    """
    После возвращения в родной город следующие 2 недели я только и делал, что спал, ел и обновлял страницу списков на поступление. Ел, пока обновлял страницу, и спал, пока ел.
    
    Несмотря на то, что у меня был хорошие баллы по ЕГЭ, меня не покидало чувство тревоги за свое будущее.
    
    Я пытался отвлечь себя прогулками, играми и видосами на всем известной платформе. Но отвлекаться получалось только во время всего этого процесса.
    
    Такими темпами мне нужно потреблять контент со скоростью 60 минут/час.
    """
    with fade
    "ЗДЕСЬ НАДО ЭКРАН С ДНЕМ ЗАЧИСЛЕНИЯ"#Исправить
    with fade
    """
    В день утверждения окончательных списков поступивших я и десяток тысяч моих собратьев по счастью и несчастью собрались на одном сайте, чем его и положили.

    Через пару часов тот восстановил свои силы, и я беспокойно нашел себя на странице поступивших.

    Это было большим облегчением, будто с меня сняли кандалы “неудачника” и накачали гелием.

    Я бы сказал, появилось ощущение невесомости
    """
    "~Наконец-то, Я - СТУДЕНТ~"
    """
    Моей радости не было предела, казалось, это был переломный момент моей жизни.
    
    Вокруг ничего не произошло, было тихо. Только ветер за окном наигрывал свои бесконечные мотивы.
    
    Внутри меня прорвало эмоциональную трубу. С самых пяток и до уровня глаз меня наполняла радость и гордость. На уровне глаз все полилось наружу.
    
    Это и правда очень значимый для меня момент.
    
    Мне скорее хотелось поделиться этим с родными.
    
    ~Первым делом нужно позвонить отцу. Мне кажется, что он ждал и желал этого больше, чем я.~
    """
    "ГУДКИ ТЕЛЕФОНА MP3 ЗДЕСЬ"#Исправить
    p "Алё, привет"
    f "Ооо, здравствуй Саш, как у тебя дела?"
    p "Я теперь не просто Саша, я – Александр, студент первого курса направления Программная инженерия!"
    f "Ёк макарёк, вот это даа! Поздравляю тебя, вступаешь на новый этап, молодец. Значит сегодня жди меня с тортиком, это нужно отметить."
    p "Заметано, жду."
    "ГУДКИ ТЕЛЕФОНА MP3 ЗДЕСЬ"#Исправить
    """
    Очень не люблю телефонные звонки, особенно когда эти звонки исходят откуда-то извне на мой телефон и это заставляет его орать своим убогим рингтоном, жужжать, будто его кто то ужалил, или он и является тем, кто жалит. Жалит и не жалеет мой слух.
    
    ~Что-то я вспылил, видать разволновался.~
    
    Следующей была мама. Ей очень понравилось то направление, которое я выбрал. Мне кажется, она будет счастлива услышать, что я поступил туда, куда хочу.
    """
    "ГУДКИ ТЕЛЕФОНА MP3 ЗДЕСЬ"#Исправить
    m "Алло, привет Саш"
    p "Привет, мам. Ты не поверишь, что произошло"
    m "Ты о своем поступлении на Программную инженерию?"
    p "КАК ТЫ УЗНАЛА?"
    m "Только что звонил отец, голос у него был очень довольный, я сразу поняла, что произошло что-то хорошее."
    m "Похвастался мне про твое поступление, сказал, как горд тобой и чуть слезу не пустил, на сколько я слышала."
    p "Серьезно? Со мной он говорил очень сдержанно."
    m "Твой отец хоть и выглядит сурово, на самом деле очень чувственный человек и он очень рад за тебя и за твой успех."
    m "Поздравляю с поступлением! На семейном ужине надо будет обсудить тему твоего переезда и финансирования. Кушать же что-то нужно."
    p "Успеется. А сейчас можно порадоваться и хорошенечко отдохнуть."
    m "Ну отдыхай, давай, до вечера."
    p "Пока."
    """
    По моей матери не видно, но она любит держать все под контролем, строить планы и т.д. Не удивительно, что они с отцом сошлись, ведь он такой же.
    
    Следом я обзвонил обоих бабушек, дедушку и наконец своего дядю, с которого все началось.
    
    С ним у нас получился забавный и довольно душевный разговор.
    
    Он дал мне парочку советов по поводу общажной жизни, выбора друзей и прохождения обучения. Очень полезные, между прочим. Мы пообещали друг другу созваниваться почаще.
    """
    with fade
    scene black
    "Неделю спустя"
    with fade
    scene room
    """
    Тем же вечером мы отпраздновали это событие. Обычный праздничный ужин. Точнее особенный.
    
    Прошла уже неделя с того момента, я пару раз встретился с друзьями. Почти все поступили куда хотели, кто-то устроился на работу, а кому-то захотелось отдохнуть от учебы. В общем каждый двигался в своем направлении.
    
    Это меня порадовало и опечалило в тот же миг.
    
    Что ж, пора до собирать вещи. Многое из того, что необходимо я собрал в порыве радости в тот же день.
    
    Зубная щетка – один из важнейших предметов современности.
    
    Дальше на очереди все остальные предметы личной гигиены.
    
    Средство для чистки лица, средство для чистки посуды, средство для чистки труб, средство для чистки средства для чистки труб…
    """
    with fade
    scene black
    "Спустя какое-то время..."
    with fade
    scene room
    """
    В моей комнате творился настоящий хаос, так как мои родители всячески настаивали на помощи в сборах.
    
    Когда дело доходит до собирания, мы все медленно сходим с ума.
    
    Каждый просил взять вещь, без которой, как им казалось, мне нет жизни на земле.
    
    Некоторые из них я все-таки взял, но цветок в горшке, ковер со стены и кота я решил оставить дома. Как бы меня ни уговаривали.
    
    Получилось так, что мама обиделась на меня, отец сказал делать что угодно, а кот в это время мирно полизывал свой длинный хвост и был доволен.
    
    СОБРАВ ВСЕ НЕОБХОДИМОЕ, Я ГОТОВИЛСЯ КО СНУ
    
    На сегодня сборы подошли к концу, я почти не вышел из ума, мои родители были рады, что все закончилось.
    """
label train_station_second:
    with fade
    scene station
    """
    Перед отъездом я захотел перекусить.
    
    Благо неподалеку была лавка с выпечкой. Там я прикупил вкуснейший беляш из когда-либо созданных. Его формы возбуждали. Возбуждали аппетит. Начинка отзывалась холестерином в моем сердце. Непередаваемые ощущения. Словно прыщ выдавить
    """
    "ЗВУК ОБЪЯВЛЕНИЯ МП3"#Исправить
    
    "Громкоговоритель" "…Уважаемые пассажиры, начинается посадка на поезд номер 321, просьба пройти на платформу №2"
    """  
    ~Надо же, сегодня я точно не опоздаю~
    
    Но я решил не торопиться, ведь посадка только началась…
    """
    with fade
    scene black
    "20 минут спустя"
    with fade
    scene station
    "ТУТ В СЦЕНАРИИ ПРОСТО БУКВА h"
    "ЗВУК ПОЕЗДА МП3" #Исправить
label hostel:
    with fade
    scene corridor
    "ОТ РАЗРАБА: МОЖЕТ ТУТ ФОН НАРИСОВАТЬ, ГДЕ МНОГО ЛЮДЕЙ КАКИХ-ТО В КОРРИДОРЕ СТОИТ? ЧТОБЫ ОН РЕАЛЬНО С КЕМ-ТО ПОЗНАКОМИЛСЯ, ТИПО КАК СТОЛОВКА В БЛе БЫЛА"
    #show neighbour at left
    """
    Отлично, я добрался до общаги к 2-м часам дня. И вот-вот нас должны начать заселять. Если оплачена квитанция
    
    Я сделал это через мобильное приложение, чтобы никуда не ходить.
    
    Ожидая своего зачисления я познакомился с парой ребят.
    
    Иногда мне кажется, что я слишком общительный, но это мне никак не мешает. Даже наоборот.
    
    Сегодня все меньше людей может похвастаться таким навыком, а в совокупности с чувством такта – это великое преимущество.
    
    Так вот, попался мне на глаза один тип. Спортивный костюм от ададис, короткая стрижка, плевал через дырку в зубе и мог лузгать целый версток семечек за долю секунды.
    
    Кажется, в мире нет равных по скорости этого действа.
    
    С виду очень мутный тип.
    
    Скажу откровенно, не хотел бы я быть тем парнем, с которым его поселят.
    
    Отвлекшись от разговора своими мыслями, собеседники уже проскользнули через 3 или 4 темы и за ними было не угнаться.
    
    Я отдал инициативу разговора и периодически поглядывал на «голубиного конкурента».
    
    Прошел с десяток минут прежде, чем я услышал свое имя. За ним огласили и второго претендента на комнату.
    
    Я стал рыскать глазами по толпе в поисках движения и отклика на фамилию за мной.
    
    Тот самый спортсмен вышел вперед и с видом полного безразличия прошел в нашу комнату.
    
    Я топнул за ним.
    """
    with fade
    scene hostel
    "Пара секунд неловкого молчания. Точнее полной тишины. И тут он ее оборвал."
    "Сосед" "Меня Серый зовут. Ну это так, к слову."
    "~К какому слову?~"
    p "меня Александр. Приятно познакомиться."
    "Мы пожали друг другу руки, но сразу было понятно, что никто этого не хотел."
    n "Чур я на той, что слева"
    p "Мне нет никакой разницы, хоть 2 этажа занимай"
    """
    Это мне еще повезло. Нас двоих засунули в комнату, которая рассчитана на четверых. Редкость на сегодняшний день.
    
    В период, когда мы раскладывали вещи, я и не пытался с ним заговорить. Мы будто находились поодаль друг от друга в двух маленьких мирах.
    
    Наша комната была поделена на 2 части вдоль, у каждого был свой стол, полка и ящик. Также у нас в комнате стоял обеденный стол, если вдруг еда дойдет с кухни до нас.
    
    Мой сосед был довольно тихий, что показалось мне странным. Мне казалось, он будет вести себя более раскованно.
    
    Заканчивая разбирать вещи, мы поочередно пошли за постельным бельем.
    """
    with fade
    scene corridor
    "По пути я встретил нашу комендантшу, которая зазывала всех на общее собрание всего этажа."
    "Комендантша" "Ты чего тут ошиваешься, иди в конец коридора на собрание."
    "Комендантша" "Тук-тук-тук, заканчивайте разбирать вещи и бегом на собрание"
    """
    Противная женщина, но чего делать. Я сразу же потопал в другой конец коридора. Это была самая просторная часть этажа, сюда смогли поместиться все его обитатели.
    
    Созвав всех, тетя комендант своим внушительным голосом начала объяснять правила общежития и назначать старосту этажа.
    
    Каждый присутствующий ощутил этот холодок, что пробегал по спине с каждым произношением твердых звуков. Казалось, кто-то бьет молотом об голый бетон.
    
    Все это не задержало нас, и мы управились за 4 минуты. После чего с той же скоростью разошлись по своим комнатам, лишь бы не находиться тут.
    
    Я даже забыл куда шел. И зайдя в комнату, тут же развернулся и пошел за постельным бельем.
    
    На выходе из комнаты со всеми вещами, которые выдавались всем студентам общежития, я встретил своего соседа.
    
    Что-то слишком часто я его встречал для первого раза.
    
    Переглянувшись, я прошел дальше и забрал свой комплект белья.
    """
    with fade
    scene hostel
    """
    В комнате было спокойно, когда я вернулся. Мой сосед уже куда-то ушел, а я развалился на первом этаже кровати и представил, что эта комната только моя.
    
    Уже завтра у нас должно пройти мероприятие «Знакомство с факультетом», и мне оставалось только ждать его в своей новой комнате.
    
    Я даже не заметил, как уснул спустя полчаса своего дуракаваляния.
    """
    with fade
    """
    Я проснулся и не заметил уже куда-то пропавшего соседа.
    
    Наверно он еще не приходил.
    
    Я сделал все утренние процедуры и был готов к мероприятию.
    
    Оно проходило в здании главного корпуса университета.
    
    Мне пришлось одеться в свои самые официальные костюмы и быть примерным студентом. Посмотрев в зеркало, я не узнал сам себя. Это был человек с обложки студенческого флаера-зазывателя для абитуриентов.
    
    ~Мой образ идеален.~
    """
    with fade
    scene street3
    """
    Я вышел на летнюю улицу и уверенно зашагал в сторону университета.
    
    Погода была легка, ветер не давал застаиваться воздуху, а облака, что закрывали солнце, сменяли друг друга с небольшой периодичностью.
    
    Уверенная походка доставляла мне небольшое неудобство. Спина сопротивлялась моему выпрямлению, поэтому это выглядело, будто я танцую плечами в стиле «робот».
    
    Между общежитием и университетом было всего 15 минут ходьбы обычным шагом и 10 минут быстрым.
    
    Расстояние до университета играет большую роль в жизни студента.
    
    В школе существовало такое поверье, так называемое «Проклятие ближеживущего». Те, кто жил ближе всех, больше всех опаздывали. Следовательно те, кто дальше жил, почти не опаздывал, ибо они выходили сильно раньше своих сопримеровцев.
    
    К счастью (или к сожалению) у студента это правило работает немного иначе
    
    Тот, кто живет близко, частенько опаздывают. Но живущие далеко на пары не приходят. И где тут правда?
    """
label uni_firstday:
    with fade
    scene uni inside
    "Мои мысли затянулись до главного входа университета. "
    with fade
    scene auditory1
    """
    Я слился с потоком проходящих студентов, волна донесла меня до моей аудитории, где я занял свое место.
    
    В аудиторию вошел невысокий темноволосый средних лет мужчина в костюме. Студенты немного притихли. Это были ребята моего направления.
    """
    "Преподаватель""Здравствуйте, дорогие студенты. С недавнего времени вы были зачислены на направление Программной инженерии. Это похвально."
    "Преподаватель""Сегодня я хотел бы вам рассказать о вашем направлении поподробнее. В самом конце у нас будет время, чтобы ответить на ваши вопросы. Итак, начнем…"
    """  
    Следующий час был наполнен рассказом о том, как мы будем постигать науку, по рецепту один к одному разведенного с водой.
    
    По окончании мероприятия все поспешили покинуть актовый зал и вкусить последние кусочки уходящего лета.
    """
    with fade
    scene uni inside
    """
    Но на выходе нас поджидало продолжение мероприятия. Между колоннами располагались группки по 3 человека в каждой. Над их головами были подняты таблички с номером группы.
    
    По этим группам нас распределили еще при поступлении.
    
    Я причалил к табличке со знакомым номером и парень в очках, один из троих представителей, начали знакомство
    """
    mih "Приветствую всех, меня зовут Михаил, в этом году я буду вашим наставником."
    krist "А меня Кристина, уверена, что мы с вами подружимся."
    "Перехватила Девушка, стоящая рядом"
    mih "Я же просил чуть-чуть подождать, теперь они подумают, что мы не серьезные."
    krist "Ну, а чего ты затягиваешь?"
    "Словесный пинг-понг продолжался до момента, пока третий не хмыкнул."
    "Третий?" """В общем, мы ваши наставники, готовы показать все интересующие вас места, и постараться отвечать на любой интересующий вас вопрос когда угодно.

    Можно сказать, что мы справочники студенческой жизни. Поделимся секретами сдачи сессии и необходимыми материалами.

    Также будем уведомлять о предстоящих мероприятиях и любых других внеучебных действах
    """
    """
    ~Классно придумано, ничего не скажешь. Кто как не второкурсники знают, что нужно первокурснику.~
    
    Они пригласили нас посидеть после мероприятия в каком-нибудь антикафе, но мне нужно было прикупить пару вещей до начала учебного года.
    
    Возможность посидеть с ними я не упустил, и сразу после дел я присоединился к ним.
    """
    with fade 
    scene hostel
    """
    Тем же вечером я лежал у себя на кровати и размышлял о том, как будет проходить мое обучение.  С кем я познакомлюсь и кто станет моим другом.
    
    Возможно большая часть всего обучения станет бесконечной рутиной, изредка прерывающейся праздниками и каникулами.
    
    А может не найдется такой тусовки, которая будет проходить без меня. У меня появится куча друзей и приятелей, я разбогатею выиграв в лотерею миллион долларов.
    
    Ладно, последнее было лишним. Ну, а что? Такое тоже случается.
    
    Уже через несколько дней у меня начинается настоящая студенческая жизнь.
    
    Первое сентября и большое количество свежих умов войдут в здание университета.
    
    Преподаватели и лекции. Никаких уроков, только пары. Большая перемена в 45 минут.
    
    Эх, стану старцем, буду также лежать и вспоминать, о чем же я думал перед тем, как стал студентом и все в этом духе.
    
    Мою мысль прервал сосед, который вернулся, чтобы немного поспать.
    
    Часто же он отсутствует.
    
    Я не упустил возможности перекинуться парой слов.
    """
    p "Представляешь, через несколько дней мы начнем обучение. Может это самый серьезный шаг в нашей жизни"
    "Начал я, будто мы друзья с самого детства."
    n "*Храп*"
    p "Да, я тоже согласен с тобой. Надо хорошенько выспаться."
    "Я выключил свет и повернулся к стене лицом. Мои высказывания разразились похрапыванием."