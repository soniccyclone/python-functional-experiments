print("hello, world")


def plus(*args):
  return sum(args)


def first(*args):
  return args[0]


def rest(*args):
  return args[1:]


def minus(*args):
  return first(*args) - plus(*rest(*args))


def inc(n):
  return n + 1


def comp(*functions):

  def begin_comp(*args):

    def inner_comp(*g):
      if len(g) == 1:
        return first(*g)(*args)
      else:
        return first(*g)(inner_comp(*rest(*g)))

    return inner_comp(*functions)

  return begin_comp


print(comp(inc, plus)(1, 2, 3))
print(plus(1, 2, 3))
print(first('a', 6))
print(rest(1, 2, 4))
print(minus(6, 1, 2))