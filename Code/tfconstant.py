import tensorflow as tf
s1 = tf.constant(7)
print(s1 + 2)

v1 = tf.constant([1, 2, 3])
print(v1 + 2)

print(v1 + s1)

v2 = v1 + s1
print(v2)

v3 = v1 + 4
print((v3))

v1 = v1 + 5
print(v1)

l1 = [ 10, 11, 12]
v1 = v1 + l1
print(v1)