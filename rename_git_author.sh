git filter-branch --commit-filter '
if [ "GIT_AUTHOR_EMAIL" = "gang.wang@shanbay.com" ];
then
    GIT_AUTHOR_EMAIL="gukz@qq.com";
    GIT_AUTHOR_NAME="gukz";
    git commit-tree "$@";
else
    git commit-tree "$@";
fi '
git push --force --tags origin 'refs/heads/*'
