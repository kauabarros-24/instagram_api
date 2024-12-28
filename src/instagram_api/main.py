from fastapi import FastAPI
import instaloader

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "system running"}

from fastapi import FastAPI, HTTPException
import instaloader

app = FastAPI()

# Inicializar Instaloader
loader = instaloader.Instaloader()

@app.get("/get_profile/{username}")
async def get_profile(username: str):
    """
    Endpoint para buscar informações de um perfil do Instagram pelo nome de usuário.
    """
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        
        return {
            "username": profile.username,
            "full_name": profile.full_name,
            "bio": profile.biography,
            "followers": profile.followers,
            "following": profile.followees,
            "is_private": profile.is_private,
            "is_verified": profile.is_verified,
            "profile_pic_url": profile.profile_pic_url,
        }
    except instaloader.exceptions.ProfileNotExistsException:
        raise HTTPException(status_code=404, detail="Profile not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    