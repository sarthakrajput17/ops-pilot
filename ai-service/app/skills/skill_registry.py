from app.models.skill_type import SkillType

from app.skills.general_skill import GeneralSkill
from app.skills.kubernetes_skill import KubernetesSkill
from app.skills.docker_skill import DockerSkill
from app.skills.terraform_skill import TerraformSkill
from app.skills.github_skill import GithubSkill


class SkillRegistry:

    def __init__(self):
        self.skills = {
            SkillType.GENERAL: GeneralSkill(),
            SkillType.KUBERNETES: KubernetesSkill(),
            SkillType.DOCKER: DockerSkill(),
            SkillType.TERRAFORM: TerraformSkill(),
            SkillType.GITHUB: GithubSkill(),
        }

    def get(self, skill_type: SkillType):
        return self.skills[skill_type]