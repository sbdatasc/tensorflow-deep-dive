1. Is tf.constant immutable as in can the value be changed in tensor generated using tf.constant?

Ans . tensors generated using tf.constant are immutable. 
        they don't have .assign() function implemented like tf.Variable
        Both tf.constant and tf.Variable don't allow for direct assignment
        x = tf.constant([1, 2, 3])
        x[0] = 5 
        This will throw an error
        
        Similarly 
        y = tf.Variable([1, 2, 3])
        y[0] = 5
        will also throw an error.



Note: All eager tf.Tensor values are immutable (in contrast to tf.Variable). There is nothing especially constant about the value returned from tf.constant. This function is not fundamentally different from tf.convert_to_tensor. The name tf.constant comes from the value being embedded in a Const node in the tf.Graph. tf.constant is useful for asserting that the value can be embedded that way.

*this above note needs further exploration*




