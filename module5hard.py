import time
class User:
    def __init__(self,nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.current_user = None
        self.videos = []

    def log_in(self, nickname, password):
        Success = True
        for i in range(len(self.users)):
            if nickname == self.users[i].nickname and hash(password) == hash(self.users[i].password):
                self.current_user = nickname
            else:
                Success = False
        if Success == False:
            print(f'User nickname {nickname} do not exist/password {password} is incorrect')

    def register(self, nickname, password, age):
        search_user = False
        new_user = User(nickname, password, age)
        for i in range(len(self.users)):
            if self.users[i].nickname == nickname:
                search_user = True
        if search_user == True:
            print(f'User {nickname} already exist')
        else:
            self.users.append(new_user)
            self.current_user = new_user.nickname

    def log_out(self):
        self.current_user = None
        print('You are logged out')

    def add(self, *videos):
        for video in videos:
            if not any(video.title == v.title for v in self.videos):
                self.videos.append(video)
            else:
                print(f'video with this title has already been added')

    def get_videos(self, search_word):
        search_result = []
        for i in range(len(self.videos)):
            if search_word.upper() in self.videos[i].title.upper():
                search_result.append(self.videos[i].title)
        return search_result

    def watch_video(self, video_name):
        if self.current_user is None:
            print('To watch the video, please log in.')
        else:
            adult = False
            for a in range(len(self.users)):
                if self.current_user == self.users[a].nickname and self.users[a].age > 18:
                    adult = True
            for i in range(len(self.videos)):
                if video_name == self.videos[i].title:
                    if self.videos[i].adult_mode == False and self.videos[i].adult_mode == False:
                        for viewing in range(1, self.videos[i].duration + 1):
                            print(viewing, end=' ')
                            time.sleep(1)
                        print('End of video')
                    elif self.videos[i].adult_mode == True and adult == True:
                        for viewing in range(1, self.videos[i].duration + 1):
                            print(viewing, end=' ')
                            time.sleep(1)
                        print('End of video')
                    elif self.videos[i].adult_mode == True and adult == False:
                        print('You are under 18 years old, please leave the page')







ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')