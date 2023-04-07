# We can't just re-use it b.c. it executes the profile.d stuff! WOW!!!!

#
# Environment configuration file for the ATLAS user. Can be sourced to set up
# the analysis release installed in the image.
#

# Execute all of the environment setup scripts of the image/OS.
# for script in /etc/profile.d/*.sh; do
#    source ${script}
# done

# Set up a nice prompt:
export PS1='\[\033[01;35m\][bash]\[\033[01;31m\][\u AnalysisBase-$AnalysisBase_VERSION]\[\033[01;34m\]:\W >\[\033[00m\] ';

# Set up the compiler:
source /opt/lcg/binutils/*/x86_64-*/setup.sh
source /opt/lcg/gcc/*/x86_64-*/setup.sh
echo "Configured GCC from: ${CC}"

# Configure Calibration via HTTP
export PATHRESOLVER_ALLOWHTTPDOWNLOAD=1

# Set up the analysis release:
source /usr/AnalysisBase/*/InstallArea/*/setup.sh
echo "Configured AnalysisBase from: $AnalysisBase_DIR"