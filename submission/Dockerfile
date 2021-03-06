#####################################################################################################################################################################
# xView2                                                                                                                                                            #
# Copyright 2019 Carnegie Mellon University.                                                                                                                        #
# NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO    #
# WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY,          # 
# EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, # 
# TRADEMARK, OR COPYRIGHT INFRINGEMENT.                                                                                                                             #
# Released under a MIT (SEI)-style license, please see LICENSE.md or contact permission@sei.cmu.edu for full terms.                                                 #
# [DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use  #
# and distribution.                                                                                                                                                 #
# This Software includes and/or makes use of the following Third-Party Software subject to its own license:                                                         #
# 1. SpaceNet (https://github.com/motokimura/spacenet_building_detection/blob/master/LICENSE) Copyright 2017 Motoki Kimura.                                         #
# DM19-0988                                                                                                                                                         #
#####################################################################################################################################################################

FROM ubuntu

# Updating the image 
RUN apt update && \
    apt install -y apt-transport-https

# Installing all dependencies 
RUN apt install -y python3 python3-pip curl git

# Making python3 the default Python 
RUN ln -s /usr/bin/python3 /usr/bin/python

# Running the rest as non-root
RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser && \
    mkdir -p /home/appuser/.keras/models && \
    usermod -a -G sudo appuser && \
    chown -R appuser:appuser /home/appuser

ADD https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5 /home/appuser/.keras/models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5

RUN chmod -R 777 /home/appuser/

USER appuser

SHELL ["/bin/bash", "-c"]

# Making the appropate directories for the inference code, inputs, and outputs
RUN mkdir -p ~/code/xview-2/
RUN mkdir -p ~/submission/ 
RUN mkdir -p ~/output/ 

RUN pip3 install numpy
RUN pip3 install -U "tensorflow==1.*"
RUN pip3 install matplotlib tqdm libtiff scipy Pillow scikit-image opencv-python imgaug IPython geopandas keras imantics simplification scikit-learn chainer tensorboard tensorboardX

#ADD xview-2 /code/xview-2/
RUN git clone https://github.com/catskillsresearch/xview2-catskills.git ~/code/xview-2

# Grabbing weights for our models
# UNCOMMENT THIS WHEN REPO/WEIGHTS ARE PUBLIC

RUN curl -L https://github.com/catskillsresearch/xview2-catskills/releases/download/v_catskills_0.0.0/localization.hdf5 -o ~/code/xview-2/weights/localization.h5
RUN curl -L https://github.com/catskillsresearch/xview2-catskills/releases/download/v_catskills_0.0.0/classification.hdf5 -o ~/code/xview-2/weights/classification.hdf5

# Finally running the container with the run.sh wrapper script to pass the CLI arguments to inference.sh
RUN chmod +x ~/code/xview-2/submission/run.sh
ENTRYPOINT ["/home/appuser/code/xview-2/submission/run.sh", "/home/appuser/code/xview-2/"]
