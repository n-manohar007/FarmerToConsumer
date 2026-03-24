
class Config:
    SECRET_KEY = "your_secret_key_here"

    MONGO_URI = (
        "mongodb+srv://manoharnellikondi1_db_user:KRXLVEctmS9bk0y3"
        "@cluster0.2mza3bb.mongodb.net/farm_fresh"
        "?retryWrites=true&w=majority&appName=Cluster0"
    )

    DEBUG = True

    # ✅ Cashfree Config
    CASHFREE_CLIENT_ID = "TEST11026123bbeb4915a6dbb64a2f7632162011"
    CASHFREE_CLIENT_SECRET = "cfsk_ma_test_da5ced1b13eb044f89b024e2df2bf17d_81ac582f"
    CASHFREE_ENVIRONMENT ="sandbox"
    UPLOAD_FOLDER = "static/uploads"
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}




