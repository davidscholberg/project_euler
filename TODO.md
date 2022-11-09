* Evaluate the usage of returning nested iterators from generator functions.
    * In some cases, a list or tuple may already exist in memory, in which case it's better for the caller to decide if the iterator object from the list or tuple is wanted.
* Evaluate the specificity of types hints.
    * Type hints should be as specific as possible, particularly for callable parameters.