// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VoteSecurise {
    struct Electeur {
        bool estEnregistre;
        bool aVote;
    }

    struct Candidat {
        string nom;
        uint256 votes;
    }

    address public administrateur;
    mapping(address => Electeur) public electeurs;
    Candidat[] public candidats;

    constructor(string[] memory nomsCandidats) {
        administrateur = msg.sender; // L'adresse qui déploie le contrat devient l'administrateur
        for (uint256 i = 0; i < nomsCandidats.length; i++) {
            candidats.push(Candidat({
                nom: nomsCandidats[i],
                votes: 0
            }));
        }
    }

    modifier seulementAdmin() {
        require(msg.sender == administrateur, "Seul l'administrateur peut appeler cette fonction.");
        _;
    }

    function enregistrerElecteur(address _electeur) public seulementAdmin {
        require(!electeurs[_electeur].estEnregistre, "Electeur deja enregistre.");
        electeurs[_electeur].estEnregistre = true;
    }

    function voter(uint256 _indexCandidat) public {
        require(electeurs[msg.sender].estEnregistre, "Vous n'etes pas enregistre pour voter.");
        require(!electeurs[msg.sender].aVote, "Vous avez deja vote.");
        require(_indexCandidat < candidats.length, "Candidat invalide.");

        electeurs[msg.sender].aVote = true;
        candidats[_indexCandidat].votes += 1;
    }

    function voirResultats() public view returns (string[] memory, uint256[] memory) {
        string[] memory noms = new string[](candidats.length);
        uint256[] memory votes = new uint256[](candidats.length);

        for (uint256 i = 0; i < candidats.length; i++) {
            noms[i] = candidats[i].nom;
            votes[i] = candidats[i].votes;
        }

        return (noms, votes);
    }
}