from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature) -> None:
        pass


# ================= NORMAL =================

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature) -> None:
        print(creature.attack())


# ================= AGGRESSIVE =================

class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return hasattr(creature, "transform") and hasattr(creature, "revert")

    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


# ================= DEFENSIVE =================

class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return hasattr(creature, "heal")

    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())