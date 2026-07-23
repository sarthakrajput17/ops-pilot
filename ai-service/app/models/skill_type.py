from enum import Enum


class SkillType(str, Enum):
    GENERAL = "general"
    KUBERNETES = "kubernetes"
    DOCKER = "docker"
    TERRAFORM = "terraform"
    GITHUB = "github"