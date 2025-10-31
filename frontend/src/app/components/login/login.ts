import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.html',
  styleUrls: ['./login.scss'],
  imports: [FormsModule, CommonModule],
  standalone: true
})
export class LoginComponent {
  username = '';
  password = '';
  error: string | null = null;

  constructor(private authService: AuthService, private router: Router) {}

  onLogin() {
    this.authService.login(this.username, this.password).subscribe({
    next: (response) => {
    this.error = null;
    
    this.router.navigate(['/treinamentos']); 
    },
    error: (err) => {
      this.error = 'Usuário ou senha incorretos';
      console.error(err);
      }
    });
  }
}

