# hello
git clone <git link> = download git repository to own computer(make sure first cd to the right folder)
git add <filename> =  add files to be committed
git commit -m "message" = commit with a message 
git status = check status
git push = push to github
git commit -am "message" = add all files that have been changed and commit all of them
git pull = download the latest changes

git log = track all the commits
git reset --hard <commit> = revert back to <commit> given in git log
git reset --hard orgin/master = reset back to whatever is on github   
    

Merge Conflict
<<<<<<<
<Your changes>
=======
<other person's changes>
>>>>>>>

[fix conflict and push again]


Making Changes
Branching 
main branch = default branch
feature branch = some other feature branch
HEAD points to the current branch
merge branch at the end when they are both done

git branch = tell you what branch your currently on and what branch exist (star and green is current branch)
git checkout -b <name of new branch> = create a new branch
git checkout <name of branch to switch to> = switch to different branch
git merge <branch name to be meraged into the current branch> = merges another branch with current branch

[fix merge conflict and commit]


Fork
copy an existing repository by clicking the Fork button and making changes to it on your own, and ask for pull request to merge your code into the master code


GitHub Pages
free way to deploy a website
create a new repository named <your username>.github.io
clone it and add your website pages
settings -> github pages is ready to be published
