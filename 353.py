class SnakeGame:
  def __init__(self, width: int, height: int, food: List[List[int]]):

    self.width = width
    self.height = height
    self.food = food
    self.num = 0
    self.a = 0  # food's index
    self.lookup = set([self.getId(0, 0)])
    self.body = collections.deque([self.getId(0, 0)])  

  def move(self, direction: str) -> int:
   
    i = self.body[0] // self.width
    j = self.body[0] % self.width

    if direction == "U":
      i -= 1
      if i < 0:
        return -1
    if direction == "L":
      j -= 1
      if j < 0:
        return -1
    if direction == "R":
      j += 1
      if j == self.width:
        return -1
    if direction == "D":
      i += 1
      if i == self.height:
        return -1

    newHead = self.getId(i, j)

    # Case 1
    if self.a < len(self.food) and i == self.food[self.a][0] and j == self.food[self.a][1]:
      self.lookup.add(newHead)
      self.body.appendleft(newHead)
      self.a += 1
      self.num += 1
      return self.num

    # Case 2
    if newHead != self.body[-1] and newHead in self.lookup:
      return -1

    # Case 3
    self.lookup.remove(self.body[-1])
    self.lookup.add(newHead)
    self.body.pop()
    self.body.appendleft(newHead)

    return self.num

  def getId(self, i: int, j: int) -> int:
    return i * self.width + j
