class Sphere:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def __str__(self):
        return f"Sphere: {self.x, self.y, self.z, self.r}"


sphere = Sphere(1, 1, 1, 2)
print(str(sphere))
