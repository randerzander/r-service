set -eu

FILES_DIR=$1
R_LIB=$2
R_LIBS_DIR=$3
REPO_URL=$4

if [ ! -d "$R_LIBS_DIR/$R_LIB" ]
then
  if [ -f "$FILES_DIR/libs/$R_LIB.tgz" ]
  then
    tar -xzvf $FILES_DIR/libs/$R_LIB.tgz -C $R_LIBS_DIR
  else
    Rscript -e 'install.packages(c("'$R_LIB'"), repos="'$REPO_URL'");'
  fi
fi
