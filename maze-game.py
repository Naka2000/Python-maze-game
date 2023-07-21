# 迷路の定義
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]
start_pos = (1, 1)  # スタート位置
end_pos = (7, 8)  # ゴール位置

# 迷路を表示する関数
def print_maze():
    for row in maze:
        print(' '.join(row))

# プレイヤーの位置
player_pos = start_pos

# ゲームのループ
while True:
    # 迷路を表示
    print_maze()

    # プレイヤーがゴールに到達した場合、ゲーム終了
    if player_pos == end_pos:
        print("ゴールに到達しました！おめでとう！")
        break

    # 移動方向の入力を受け付ける
    direction = input("移動方向を選択してください（上: w, 下: s, 左: a, 右: d）: ")

    # プレイヤーの移動
    new_pos = player_pos  # 新しいプレイヤーの位置
    if direction == "w" and maze[player_pos[0] - 1][player_pos[1]] != '#':
        new_pos = (player_pos[0] - 1, player_pos[1])
    elif direction == "s" and maze[player_pos[0] + 1][player_pos[1]] != '#':
        new_pos = (player_pos[0] + 1, player_pos[1])
    elif direction == "a" and maze[player_pos[0]][player_pos[1] - 1] != '#':
        new_pos = (player_pos[0], player_pos[1] - 1)
    elif direction == "d" and maze[player_pos[0]][player_pos[1] + 1] != '#':
        new_pos = (player_pos[0], player_pos[1] + 1)

    # プレイヤーの位置を更新
    if new_pos != player_pos:
        maze[player_pos[0]][player_pos[1]] = ' '
        player_pos = new_pos

