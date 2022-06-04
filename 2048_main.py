import random
import pygame
import math

class Map:
  def __init__(self):
    self.size = 4 # 4X4 형식
    self.score = 0 # 점수
    self.map = [[0 for i in range(4)] for i in range(4)] # 맵
    self.add1() # 초기 두개의 블럭 생성
    self.add1()
  
  def add1(self): # 초기블럭 생성(c 블럭만)
    while True:
      px = random.randint(0, 3)
      py = random.randint(0, 3)
      if self.map[py][px] == 0:
        self.map[py][px] = 2
        break
  
  def add(self): # 블럭 생성(c or c++)
    if effect:
      move.play()
    while True:
      px = random.randint(0, 3)
      py = random.randint(0, 3)
      if self.map[py][px] == 0:
        x = random.randint(0, 3) > 0 and 2 or 4
        self.map[py][px] = x
        break
  
  
  #       ，                 ，        
  def adjust(self): # 합치기
    changed = False # 합쳐졌는지 판별
    for a in self.map:
      b = []
      last = 0
      for v in a:
        if v != 0:
          if v == last:
            b.append(b.pop() << 1)
            self.score += v * 2 # 합쳐서 만들어진 숫자만큼 점수 추가
            last = 0
          else:
            b.append(v)
            last = v
      b += [0] * (self.size - len(b))
      for i in range(self.size):
        if a[i] != b[i]:
          changed = True 
      a[ : ] = b
    return changed

  def rotate90(self):
    self.map = [[self.map[c][r] for c in range(self.size)] for r in reversed(range(self.size))]
  
  #       
  def over(self): # 게임 오버 판별
    for r in range(self.size):
      for c in range(self.size):
        if self.map[r][c] == 0:
          return False
    for r in range(self.size):
      for c in range(self.size - 1):
        if self.map[r][c] == self.map[r][c + 1]:
          return False
    for r in range(self.size - 1):
      for c in range(self.size):
        if self.map[r][c] == self.map[r + 1][c]:
          return False
    return True
    
  def moveUp(self):
    if self.adjust():
      self.add()
  
  def moveDown(self):
    self.rotate90()
    self.rotate90()
    if self.adjust():
      self.add()
    self.rotate90()
    self.rotate90()

  def moveLeft(self):
    self.rotate90()
    if self.adjust(): #블럭이 합쳐졌다면 블럭 생성
      self.add()
    self.rotate90()
    self.rotate90()
    self.rotate90()  

  def moveRight(self):
    self.rotate90()
    self.rotate90()
    self.rotate90()
    if self.adjust():
      self.add()
    self.rotate90()  
  

  def create_block(self): #블럭 이미지 띄우기
    block = [[(37,211),(156,211),(275,211),(394,211)], # 각 블럭이 들어갈 좌표
    [(37,329),(156,329),(275,329),(394,329)],
    [(37,447),(156,447),(275,447),(394,447)],
    [(37,564),(156,564),(275,564),(394,564)] ]

    #블럭 이미지들
    block_image=["block_c.png", "block_c++.png", "block_c#.png", "block_vs.png", "block_jv.png", "block_js.png", "block_ts.png", "block_s.png", "block_php.png", "block_sql.png", "block_python.png"]#블럭 이미지들을 넣을 리스트
    b_image = []
    for i in block_image:
      b_image.append(pygame.image.load(i))

    count_x = 0 #좌표의 인덱스
    count_y = 0
    for a in self.map:
      for b in a:
        if b is not 0: # 0 이 아니라면 (2,4,8,16 ... 이라면)
          screen.blit(b_image[int(math.log2(b)) - 1], block[count_x][count_y]) 
        count_x += 1
      count_x = 0
      count_y += 1
    count_x = 0
    count_y = 0

def display_start_screen():#시작화면
  pygame.display.set_caption("2048 START")
  global start_button #시작버튼 전역 선언
  background = pygame.image.load("start_screen.jpg") #시작화면 이미지
  screen.blit(background, (0,0)) # 이미지 적용
  start_button = pygame.Rect(146, 549, 250 , 100) #시작 버튼 위치 설정

def display_game_screen():#게임메인 화면
  pygame.display.set_caption("2048")
  global option_button #옵션 버튼 전역 선언
  global undo_button #언두 버튼 
  global score_button 
  background = pygame.image.load("main.jpg") #게임화면 이미지
  screen.blit(background, (0,0)) # 이미지 적용
  option_button = pygame.Rect(460, 130, 50 , 50) # 각 버튼 위치 설정
  undo_button = pygame.Rect(367, 128, 54, 54)
  score_button = pygame.Rect(355, 74, 53, 29) 
  score_font = pygame.font.Font(None, 30)
  score = score_font.render(str(map.score), True, (0,0,0))
  screen.blit(score, (368, 85))

def display_rank_screen(): # 랭킹화면
  global rank_quit_button # 랭킹화면에서 나가는 버튼
  global rank_restart_button
  pygame.display.set_caption("2048 RANKING")
  background = pygame.image.load("Ranking.png") # 이미지 로드
  screen.blit(background, (0,0)) # 이미지 적용
  
  board = open("ranking.txt", "r")     #순위표 open
    
  rankinglist = []     #순위를 담을 리스트 생성, 형식: ['이름', '점수']

  BLACK = (0, 0, 0)

  while True:
      line = board.readline()     #txt파일에서 한 줄씩 읽어오기

      if not line:     #txt 파일에서 읽어올 것이 없어, line이 비었다면, 중단
          break

      line = line.split()     #['이름 점수'] 형태를 ['이름', '점수'] 형태로 쪼개기
      rankinglist.append(line)     #rankinglist에 삽입
      
  board.close()     #txt파일 닫기
  
  y = 250     #텍스트가 출력될 y좌표, x는 변화가 없으므로 아래 반복문에서는 상수로 직접 입력
  for i in range(5):     #텍스트 출력
      myFont = pygame.font.SysFont( "arial", 30, True, False)
      name = myFont.render(rankinglist[i][0], True, BLACK)
      score = myFont.render(rankinglist[i][1], True, BLACK)

      screen.blit(name, [210, y])
      screen.blit(score, [340, y])
      y += 68
  
  rank_quit_button = pygame.Rect(387, 660, 132, 42) # rank_quit버튼 위치 설정
  rank_restart_button = pygame.Rect(242, 660, 132, 42)

def display_game_over():
  pygame.display.set_caption("GAME OVER")
  global click_button 
  background = pygame.image.load("game_over.jpg") # 게임오버 배경이미지 로드
  screen.blit(background, (0,0)) # 게임오버 배경 이미지 적용
  score_font = pygame.font.Font(None, 40)
  score = score_font.render(str(map.score), True, (0,0,0))
  screen.blit(score, (325, 253))

  click_button = pygame.Rect(358,635,155,63)

def display_clear_screen():
  pygame.display.set_caption("CLEAR!")
  global clear_button
  background = pygame.image.load("clear.png") # 옵션 배경이미지 로드
  screen.blit(background, (0,0)) # 옵션 배경 이미지 적용

  clear_button = pygame.Rect(420,680,105,30)



def display_option_screen():
  pygame.display.set_caption("2048 OPTION")
  global option_quit_button # 옵션 내부 버튼들 전역 선언
  global bgm_button
  global sound_button
  global restart_button
  background = pygame.image.load("option.png") # 옵션 배경이미지 로드
  screen.blit(background, (0,0)) # 옵션 배경 이미지 적용

  sound_button = pygame.Rect(130,216,94,94)
  bgm_button = pygame.Rect(316, 216, 94, 94)
  restart_button = pygame.Rect(130, 404, 280, 93)#restart버튼
  option_quit_button = pygame.Rect(130, 541, 280, 93)# 옵션 종료 버튼

pygame.mixer.pre_init()  
pygame.init()
pygame.mixer.music.load("bgm.wav")
button_sound = pygame.mixer.Sound("button_se.wav")
move = pygame.mixer.Sound("action_Se.wav")
pygame.mixer.music.play(-1)
screen_width = 540 # 스크린 화면 크기 (540 X 725)
screen_height = 725

clock = pygame.time.Clock() # 블럭 이동 속도 조절을 위한 clock

screen = pygame.display.set_mode((screen_width, screen_height))#배경

start = False # 시작화면 트리거
running = True 
option = False # 옵션화면 트리거
rank = False # 랭킹화면 트리거
bsound = True
effect = True
while running:
  click_pos = None # 클릭 좌표
  clock.tick(10)# 속도 조절

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONUP: # 마우스 버튼 클릭하면
      click_pos = pygame.mouse.get_pos() # 마우스 좌표를 click_pos에 저장

  if click_pos:
    if start_button.collidepoint(click_pos): # 시작 버튼을 누르면 start를 True로
      if effect:
        button_sound.play()
      if start == False:
        map = Map()
      start = True
      
  
  if start: # 게임이 시작되면
    if option: # 옵션화면 일때
      display_option_screen()

      if click_pos:
        if bgm_button.collidepoint(click_pos):
          if effect:
            button_sound.play()
          if bsound:
            pygame.mixer.music.pause()
            bsound = False
          else:
            pygame.mixer.music.unpause()
            bsound = True
      
      if click_pos:
        if sound_button.collidepoint(click_pos):
          if effect:
            effect = False
          else:
            effect = True
            button_sound.play()

            
      if click_pos: # 옵션 화면에서 옵션 quit버튼을 누르면 옵션을 False로
        if option_quit_button.collidepoint(click_pos):
          if effect:
            button_sound.play()
          option = False

      if click_pos: # 옵션 화면에서 옵션 quit버튼을 누르면 옵션을 False로
        if restart_button.collidepoint(click_pos):
          if effect:
            button_sound.play()
          map = Map()
          option = False

    else: # 옵션 화면이 아니라면 게임 화면
      display_game_screen()
      map.create_block() # 블럭 두개 생성
      if event.type == pygame.KEYDOWN: # 키보드를 눌렀을 때
        if event.key == pygame.K_UP: # up이면
          map.moveUp()

        elif event.key == pygame.K_DOWN: # down이면
          map.moveDown()         

        elif event.key == pygame.K_LEFT: # left로 이동 이면
          map.moveLeft()         

        elif event.key == pygame.K_RIGHT: #right로 이동이면
          map.moveRight()  
          

      for i in map.map:
        for j in i:
          if j == 2048:
            if rank: # 확인을 위한 부분 (무시해주세요)
              display_rank_screen()
              if click_pos:
                if rank_quit_button.collidepoint(click_pos):
                  if effect:
                    button_sound.play()
                  rank = False
                  start = False
              
              if click_pos:
                if rank_restart_button.collidepoint(click_pos):
                  if effect:
                    button_sound.play()

                  map = Map()
                  rank = False
                  start = False
                  start = True
                  

            else:
              display_clear_screen()
            
              if click_pos:
                if clear_button.collidepoint(click_pos): # 시작 버튼을 누르면 start를 True로
                  if effect:
                    button_sound.play()
                  rank = True




      if map.over():
        if rank: # 확인을 위한 부분 (무시해주세요)
          display_rank_screen()

          if click_pos:
            if rank_quit_button.collidepoint(click_pos):
              if effect:
                button_sound.play()
              rank = False
              start = False

          if click_pos:
            if rank_restart_button.collidepoint(click_pos):
              if effect:
                button_sound.play()

              map = Map()
              rank = False
              start = False
              start = True

        else:
          display_game_over()
          if click_pos:
            if click_button.collidepoint(click_pos): # 시작 버튼을 누르면 start를 True로
              if effect:
                button_sound.play()
              rank = True


    
      if click_pos: # 마우스를 클릭했을때
          if option_button.collidepoint(click_pos): # 옵션버튼을 누르면 옵션을 True로
            if effect:
              button_sound.play()
            option = True

  else: # default로 시자화면 출력
    display_start_screen()

  
  pygame.display.update() # 화면을 계속 띄우기 위해서 화면을 계속 업데이트 해줘야 함
  

pygame.quit() # running이 false가 되면 파이게임이 종료됨
