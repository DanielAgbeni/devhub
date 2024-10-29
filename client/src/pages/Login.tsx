import { useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { cn } from "@/lib/utils";
import { buttonVariants } from "@/components/ui/button";
import { UserAuthForm } from "@/components/Auth/user-auth-form-login";

const Login = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const storedUsername = localStorage.getItem('devhub_username');
    if (storedUsername) {
      navigate('/home');
    }
  }, [navigate]);

  return (
    <div className="container relative h-screen flex flex-col items-center justify-center lg:grid lg:max-w-none lg:grid-cols-2 lg:px-0 dark:bg-zinc-900">
      <Link
        to="/signup"
        className={cn(
          buttonVariants({ variant: "ghost" }),
          "absolute right-4 top-4 md:right-8 md:top-8"
        )}
      >
        Signup
      </Link>
      <div className="relative hidden lg:flex h-full flex-col bg-muted p-10 text-white"
        style={{
          backgroundImage: "url('https://images.unsplash.com/photo-1590212151175-e58edd96185b?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')",
          backgroundSize: 'cover'
        }}>
        <div className="relative z-20 flex items-center text-lg font-medium">
          <Link to="/" className="text-white">
            <span style={{ fontSize: '4rem' }}>dh</span>
          </Link>
        </div>
        <div className="relative z-20 mt-auto">
          <blockquote className="space-y-2">
            <p className="text-lg">
              Contributing to community feels like we are useful to others.
            </p>
            <footer className="text-sm">DevHub</footer>
          </blockquote>
        </div>
      </div>

      <div className="flex items-center justify-center w-full lg:p-8">
        <div className="mx-auto flex w-full flex-col justify-center space-y-6 sm:w-[350px]">
          <div className="flex flex-col space-y-2 text-center">
            <h1 className="text-2xl font-semibold tracking-tight">
              Login to <a href="https://www.devhub.page">DevHub</a>
            </h1>
            <p className="text-sm text-muted-foreground">
              Enter your details below to Login to your account
            </p>
          </div>
          <UserAuthForm/>
          <p className="px-8 text-center text-sm text-muted-foreground">
            By clicking continue, you agree to our{" "}
            <Link
              to="/terms-and-conditions"
              className="underline underline-offset-4 hover:text-primary"
            >
              Terms of Service
            </Link>{" "}
            and{" "}
            <Link
              to="/privacy-policy"
              className="underline underline-offset-4 hover:text-primary"
            >
              Privacy Policy
            </Link>
            .
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;
