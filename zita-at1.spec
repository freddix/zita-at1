Summary:	Zita autotuner
Name:		zita-at1
Version:	0.4.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Sounds
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	4e068b6cd9ceea981f7c9000a568fbe7
Patch0:		%{name}-make.patch
BuildRequires:	cairo-devel
BuildRequires:	clthreads-devel
BuildRequires:	clxclient-devel
BuildRequires:	fftw3-devel
BuildRequires:	freetype-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AT1 is an 'autotuner', normally used to correct the pitch of a voice
singing (slightly) out of tune.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C source \
	CXX="%{__cxx}"		\
	LDFLAGS="%{rpmldflags}"	\
	OPTFLAGS="%{rpmcflags}"	\
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT	\
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

