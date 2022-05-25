import random
import pygame

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

  for i in range(0,4): #블럭들 위치를 행렬로 이차원 리스트에 저장
    y = 211 + 118 * i
    for j in range(0,4):
      x = 37 + 119 * j
      block[i].append((x,y))
    block.append([])

def create_block_1(): #블럭 생성
  b_image.append(pygame.image.load("block_c.png"))# 블럭 이미지 순서대로 리스트에 저장
  b_image.append(pygame.image.load("block_c++.png"))
  screen.blit(b_image[0], block[loc_y[0]][loc_x[0]]) # random한 위치 두 곳에 블럭 이미지 생성
  screen.blit(b_image[0], block[loc_y[1]][loc_x[1]])
  if loc_x[0] == loc_x[1] and loc_y[0] == loc_y[1]: # 두 위치가 겹친다면 다음 단계 블럭으로 생성
    screen.blit(b_image[1], block[loc_y[0]][loc_x[0]])

def display_rank_screen(): # 랭킹화면
  global rank_quit_button # 랭킹화면에서 나가는 버튼
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

def display_option_screen():
  pygame.display.set_caption("2048 OPTION")
  global option_quit_button # 옵션 내부 버튼들 전역 선언
  global bgm_button
  global sound_button
  global restart_button
  background = pygame.image.load("option.png") # 옵션 배경이미지 로드
  screen.blit(background, (0,0)) # 옵션 배경 이미지 적용

  bgm_button = pygame.Rect(130,216,94,94)
  sound_button = pygame.Rect(316, 410, 94, 94)
  restart_button = pygame.Rect(130, 404, 280, 93)#restart버튼
  option_quit_button = pygame.Rect(130, 541, 280, 93)# 옵션 종료 버튼

pygame.init()
block = [] # 블럭의 좌표를 위한 2차원 리스트 선언
block.append([])

loc_x = [] # 블럭의 x,y좌표가 들어가는 리스트를 각각 선언,  이후 난수를 두개 넣어놓음(시작시 2개의 블럭 생성을 위해)
loc_x.append(random.randrange(0,4))
loc_x.append(random.randrange(0,4))
loc_y = []
loc_y.append(random.randrange(0,4))
loc_y.append(random.randrange(0,4))

while loc_x[0] == loc_x[1] and loc_y[0] == loc_y[1]:# 만약 초기 생성 블럭 두개의 위치가 같다면 한 블럭을 다시 생성
  loc_x[1] = random.randrange(0,4)
  loc_y[1] = random.randrange(0,4)

b_image=[]#블럭 이미지들을 넣을 리스트

screen_width = 540 # 스크린 화면 크기 (540 X 725)
screen_height = 725

clock = pygame.time.Clock() # 블럭 이동 속도 조절을 위한 clock

screen = pygame.display.set_mode((screen_width, screen_height))#배경

start = False # 시작화면 트리거
running = True 
option = False # 옵션화면 트리거
rank = False # 랭킹화면 트리거
while running:
  click_pos = None # 클릭 좌표
  clock.tick(20)# 속도 조절

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONUP: # 마우스 버튼 클릭하면
      click_pos = pygame.mouse.get_pos() # 마우스 좌표를 click_pos에 저장

  if click_pos:
    if start_button.collidepoint(click_pos): # 시작 버튼을 누르면 start를 True로
      start = True
  
  if start: # 게임이 시작되면
    if option: # 옵션화면 일때
      display_option_screen()

      if click_pos: # 옵션 화면에서 옵션 quit버튼을 누르면 옵션을 False로
        if option_quit_button.collidepoint(click_pos):
          option = False

    elif rank: # 확인을 위한 부분 (무시해주세요)
        display_rank_screen()

        if click_pos:
          if rank_quit_button.collidepoint(click_pos):
            rank = False

    else: # 옵션 화면이 아니라면 게임 화면
      display_game_screen()
      create_block_1() # 블럭 두개 생성
      if event.type == pygame.KEYDOWN: # 키보드를 눌렀을 때
        if event.key == pygame.K_UP: # up이면
          for i in range(len(loc_x)): # 블럭의 개수만큼 반복하여 모든 블럭의 y좌표를 위로 이동
            while loc_y[i] != 0: # 벽을 만날때 까지 이동
              loc_y[i] -= 1 
              

        elif event.key == pygame.K_DOWN: # down이면
          for i in range(len(loc_x)):
            while loc_y[i] != 3:
              loc_y[i] += 1          

        elif event.key == pygame.K_LEFT: # left로 이동 이면
          for i in range(len(loc_x)):
            while loc_x[i] != 0:
              loc_x[i] -= 1          

        elif event.key == pygame.K_RIGHT: #right로 이동이면
          for i in range(len(loc_x)):
            while loc_x[i] != 3:
              loc_x[i] += 1        
    
      if click_pos: # 마우스를 클릭했을때
          if option_button.collidepoint(click_pos): # 옵션버튼을 누르면 옵션을 True로
            option = True
          elif score_button.collidepoint(click_pos): # 스코어 화면 전환 디버깅을 위한 버튼
            rank = True

  else: # default로 시자화면 출력
    display_start_screen()

  
  pygame.display.update() # 화면을 계속 띄우기 위해서 화면을 계속 업데이트 해줘야 함
  

pygame.quit() # running이 false가 되면 파이게임이 종료됨
