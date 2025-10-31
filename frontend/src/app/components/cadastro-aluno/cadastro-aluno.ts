import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule,AbstractControl,ValidationErrors} from '@angular/forms';
import { AlunoService, Aluno } from '../../services/aluno'; 

@Component({
  selector: 'app-cadastro-aluno',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule], 
  templateUrl: './cadastro-aluno.html',
  styleUrls: ['./cadastro-aluno.scss']
})
export class CadastroAlunoComponent implements OnInit {

  cadastroForm!: FormGroup;
  isLoading = false;
  successMessage: string | null = null;
  errorMessage: string | null = null;

  constructor(private fb: FormBuilder, private alunoService: AlunoService) {}

  ngOnInit(): void {
    this.cadastroForm = this.fb.group({
      nome: ['', [Validators.required, Validators.minLength(3)]],
      email: ['', [Validators.required, Validators.email]],
      telefone: ['', [Validators.pattern('^\\+?\\d{10,15}$', )]], 
      password: ['', [Validators.required, Validators.minLength(6)]],
      confirmPassword: ['', Validators.required]
    }, { validators: this.passwordMatchValidator });
  }

  // Validador Customizado para checar se as senhas coincidem
  passwordMatchValidator(control: AbstractControl): ValidationErrors | null {
    const password = control.get('password')?.value;
    const confirmPassword = control.get('confirmPassword')?.value;

    return password && confirmPassword && password !== confirmPassword 
      ? { mismatch: true } 
      : null;
  }

  onSubmit(): void {
    this.successMessage = null;
    this.errorMessage = null;

    if (this.cadastroForm.invalid) {
      // Exibe erros de validação no formulário
      this.cadastroForm.markAllAsTouched();
      return;
    }

    this.isLoading = true;
    
    const { confirmPassword, ...data } = this.cadastroForm.value;
    const alunoData: Aluno = data; 

    this.alunoService.cadastrarAluno(alunoData).subscribe({
      next: (response) => {
        this.isLoading = false;
        this.successMessage = `Aluno ${response.nome} cadastrado com sucesso!`;
        
        this.cadastroForm.reset(); 
        Object.keys(this.cadastroForm.controls).forEach(key => {
            this.cadastroForm.get(key)?.setErrors(null) ;
        });
      },
      error: (error) => {
        this.isLoading = false;
        console.error('Erro no cadastro:', error);

        this.errorMessage = 'Erro no cadastro: ';
        
        // Tratamento de erros detalhados do Django DRF
        if (error.error && typeof error.error === 'object') {
            const errorMessages = [];
            for (const key in error.error) {
                if (Array.isArray(error.error[key])) {
                    errorMessages.push(`**${key}**: ${error.error[key].join('; ')}`);
                }
            }
            this.errorMessage += errorMessages.join(' | ');
        } else {
            this.errorMessage = 'Ocorreu um erro desconhecido no servidor.';
        }
      }
    });
  }
}