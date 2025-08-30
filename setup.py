from setuptools import find_packages, setup

setup(
    name="mcq_generator",
    version="0.0.1",
    author="akshat ps",
    author_email="akshatpratapsingh482002@gmail.com",
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages(),
)
