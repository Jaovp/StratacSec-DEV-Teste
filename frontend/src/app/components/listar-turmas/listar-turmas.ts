import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { TurmaService } from '../../services/turma';
import { FormsModule } from '@angular/forms';
import { TreinamentoService } from '../../services/treinamento';

@Component({
  selector: 'app-listar-turmas',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './listar-turmas.html',
  styleUrls: ['./listar-turmas.scss']
})
export class ListarTurmasComponent implements OnInit {
  turmas: any[] = [];
  treinamentoId!: number;
  treinamentoNome = '';
  loading = true;
  error = '';

  showModal = false;
  novaTurma: any = { nome: '', data_inicio: '', data_conclusao: '', link_acesso: '', treinamento: null };
  treinamentos: any[] = [];

  constructor(
    private turmaService: TurmaService,
    private treinamentoService: TreinamentoService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.treinamentoId = Number(this.route.snapshot.paramMap.get('treinamentoId'));
    this.turmaService.listarTurmas(this.treinamentoId).subscribe({
      next: (data) => {
        this.turmas = data;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Erro ao carregar turmas.';
        this.loading = false;
      }
    });

    this.carregarTreinamentos();
  }

  abrirRecursos(turmaId: number) {
    this.router.navigate(['/recursos', turmaId]);
  }

  listarTurmas() {
    this.turmaService.listarTurmas(this.treinamentoId).subscribe({
      next: (data) => (this.turmas = data),
      error: (err) => console.error(err)
    });
  }

  carregarTreinamentos() {
    this.treinamentoService.listarTreinamentos().subscribe({
      next: (data) => {
        this.treinamentos = data;
        const t = this.treinamentos.find(t => t.id === this.treinamentoId);
        if (t) {
          this.treinamentoNome = t.nome;
        }
      },
      error: (err) => console.error(err)
    });
  }

  abrirModal() {
    this.novaTurma = { nome: '', data_inicio: '', data_conclusao: '', link_acesso: '', treinamento: this.treinamentoId };
    this.showModal = true;
  }

  fecharModal() {
    this.showModal = false;
  }

  salvarTurma() {
    this.turmaService.criarTurma(this.novaTurma).subscribe({
      next: () => {
        this.fecharModal();
        this.listarTurmas();
      },
      error: (err) => console.error(err)
    });
  }
}
