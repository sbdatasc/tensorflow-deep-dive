## Definitions

scalar - a single number
        shape=() - an empty tuple
        ndim = 0.
        *Also called a 0-dimensional tensor*


vector - an array of a row of numbers i.e. shape = (n, ) where n => 0
        a vector can be created with an empty list. 
        In that case the shape will be equal to 0.
        ndim = 1.
        *Also called a 1-dimensional tensor*

matrix - an array where there are both rows and columns 
            i.e 2-dimensional
        shape = (n, m) where n => 0 and m=> 0
        ndim = 2.
        *Also called a 2-dimensional tensor*

tensor - an n-dimensional array of numbers
        shape=(n1, n2, n3, ..... nn) 
        where n is the total number of dimensions
        and n1 =>0, n2=>0, n3=>0 .... nn=>0


## tf.constant
Reference - 
1. tf.constant documentation at [tensorflow](https://www.tensorflow.org/api_docs/python/tf/constant)
2. [What is a tensor?](https://www.youtube.com/watch?v=f5liqUk0ZTw)







Creates a constant tensor from a tensor-like object.
tf.constant(
    value, dtype=None, shape=None, name='Const'
)

There is a particular note with regards to constants about tf.constant

"
Note: All eager tf.Tensor values are immutable (in contrast to tf.Variable). There is nothing especially constant about the value returned from tf.constant. This function is not fundamentally different from tf.convert_to_tensor. The name tf.constant comes from the value being embedded in a Const node in the tf.Graph. tf.constant is useful for asserting that the value can be embedded that way.

*This note will need further analysis to understand what this actually means 
"
## Random number generation

References:
1. [Set Seed](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)

Key notes on Random Generation

Operations that rely on a random seed actually derive it from two seeds: the global and operation-level seeds. This sets the global seed.

Its interactions with operation-level seeds is as follows:

1. If neither the global seed nor the operation seed is set: A randomly picked seed is used for this op.
2. If the global seed is set, but the operation seed is not: The system deterministically picks an operation seed in conjunction with the global seed so that it gets a unique random sequence. Within the same version of tensorflow and user code, this sequence is deterministic. However across different versions, this sequence might change. If the code depends on particular seeds to work, specify both global and operation-level seeds explicitly.
3. If the operation seed is set, but the global seed is not set: A default global seed and the specified operation seed are used to determine the random sequence.
4. If both the global and the operation seed are set: Both seeds are used in conjunction to determine the random sequence.
5. tf.random.uniform kernel (i.e. internal representation) is used by TensorFlow for all calls of it with the same arguments, and the kernel maintains an internal counter which is incremented every time it is executed, generating different results.
6. Use the stateless random ops such as tf.random.stateless_uniform. Also see tf.random.experimental.Generator for a new set of stateful random ops that use external variables to manage their states.

