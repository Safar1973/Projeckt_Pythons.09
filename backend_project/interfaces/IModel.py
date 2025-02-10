from abc import ABC, abstractmethod

class IModel(ABC):
    """
    Interface für alle Model-Klassen, die Datenbankoperationen durchführen.
    """

    @abstractmethod
    def find_by_id(self, entity_id):
        """
        Findet eine Entität anhand ihrer ID.

        :param entity_id: Die ID der Entität.
        :return: Die gefundene Entität oder None, falls nicht gefunden.
        """
        pass

    @abstractmethod
    def create(self, data):
        """
        Erstellt eine neue Entität in der Datenbank.

        :param data: Die Daten der Entität als Dictionary.
        :return: Die erstellte Entität oder eine Fehlermeldung.
        """
        pass

    @abstractmethod
    def update(self, entity_id, data):
        """
        Aktualisiert eine bestehende Entität anhand ihrer ID.

        :param entity_id: Die ID der Entität.
        :param data: Die aktualisierten Daten der Entität als Dictionary.
        :return: Die aktualisierte Entität oder eine Fehlermeldung.
        """
        pass

    @abstractmethod
    def delete(self, entity_id):
        """
        Löscht eine Entität anhand ihrer ID.

        :param entity_id: Die ID der Entität.
        :return: True, falls erfolgreich gelöscht, sonst False.
        """
        pass
