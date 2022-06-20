# Process

The following code snippets will be help when you have to install or reinstall Tensorflow

### check the current tensorflow version

python -m pip list | grep tensorflow
### force upgrade tensorflow-deps first
conda install -c apple tensorflow-deps --force-reinstall
### or point to specific conda environment if you have one
conda install -c apple tensorflow-deps --force-reinstall -n my_env
### uninstall existing tensorflow-macos and tensorflow-metal
python -m pip uninstall tensorflow-macos
python -m pip uninstall tensorflow-metal
### install the latest
python -m pip install tensorflow-macos
python -m pip install tensorflow-metal
### verify that you have the latest 
python -m pip list | grep tensorflow


## References
1. [Apple Developer Article](https://developer.apple.com/metal/tensorflow-plugin/)
2. [Apple Developer Forum](https://developer.apple.com/forums/thread/691578)