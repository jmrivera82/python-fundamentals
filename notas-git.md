#Vinculación vía SSH
ssh-keygen -t ed25519 -C "tu_email_de_github"

## Si ya hay clave SSH

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub

##Verificar conexión

ssh -T git@github.com

##instalar gh para crear repositorio desde consola

sudo apt install gh
gh auth login
gh auth status

git init
git add .
git commit -m "initial commit"

gh repo create python-fundamentals --public --source=. --remote=origin --push

##Si origin ya existe
git remote remove origin
gh repo create python-fundamentals --public --source=. --remote=origin --push


##Cambiar remoto https --> SSH
git remote set-url origin git@github.com:USUARIO/REPO.git
git remote -v


#Convención Git para commits
feat: Nueva característica.
fix: Corrección de un error.
docs: Cambios en la documentación.
style: Cambios de formato, espacios, etc. (no afecta código).
refactor: Cambio de código que no corrige error ni añade funcionalidad.
perf: Mejora de rendimiento.
test: Añadir o corregir pruebas.
chore: Tareas de mantenimiento o herramientas (build, dependencias).

#Comandos

git pull: sincroniza repositorio remoto con el local

	git pull --rebase aplica los cambios locales encima de los cambios remotos descargados

git fecth
git merge
git 
