import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { TreinamentoService } from '../../services/treinamento';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-listar-treinamentos',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './listar-treinamentos.html',
  styleUrls: ['./listar-treinamentos.scss']
})
export class ListarTreinamentosComponent implements OnInit {
  treinamentos: any[] = [];
  loading = true;
  error = '';
  isAdmin = false;
  showModal = false;
  novoTreinamento = { nome: '', descricao: '' };

  constructor(
    private treinamentoService: TreinamentoService, private router: Router) {}

  ngOnInit(): void {
    this.treinamentoService.listarTreinamentos().subscribe({
      next: (data) => {
        this.treinamentos = data;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Erro ao carregar treinamentos.';
        this.loading = false;
      }
    });
  }

  abrirTurmas(treinamentoId: number) {
    this.router.navigate(['/turmas', treinamentoId]);
  }

  abrirModal() {
    this.showModal = true;
  }

  fecharModal() {
    this.showModal = false;
    this.novoTreinamento = { nome: '', descricao: '' };
  }

  salvar() {
    this.treinamentoService.criar(this.novoTreinamento).subscribe({
      next: () => {
        this.fecharModal();
        this.treinamentoService.listarTreinamentos().subscribe({
          next: data => this.treinamentos = data
        });
      },
      error: err => console.error(err)
    });
  }

}
