#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtquickcontrols
Version  : 5.12.0
Release  : 14
URL      : https://download.qt.io/official_releases/qt/5.12/5.12.0/submodules/qtquickcontrols-everywhere-src-5.12.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.12/5.12.0/submodules/qtquickcontrols-everywhere-src-5.12.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0 OFL-1.0
Requires: qtquickcontrols-lib = %{version}-%{release}
Requires: qtquickcontrols-license = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5QuickWidgets)
BuildRequires : pkgconfig(Qt5Sql)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)

%description
ABOUT
This project aims to deliver widgets/controls functionality with Qt Quick.

%package lib
Summary: lib components for the qtquickcontrols package.
Group: Libraries
Requires: qtquickcontrols-license = %{version}-%{release}

%description lib
lib components for the qtquickcontrols package.


%package license
Summary: license components for the qtquickcontrols package.
Group: Default

%description license
license components for the qtquickcontrols package.


%prep
%setup -q -n qtquickcontrols-everywhere-src-5.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1544051223
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtquickcontrols
cp LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtquickcontrols/LICENSE.FDL
cp LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtquickcontrols/LICENSE.GPL2
cp LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtquickcontrols/LICENSE.GPL3
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtquickcontrols/LICENSE.GPL3-EXCEPT
cp LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtquickcontrols/LICENSE.LGPL3
cp examples/quickcontrols/extras/dashboard/fonts/LICENSE %{buildroot}/usr/share/package-licenses/qtquickcontrols/examples_quickcontrols_extras_dashboard_fonts_LICENSE
cp examples/quickcontrols/extras/gallery/fonts/LICENSE.txt %{buildroot}/usr/share/package-licenses/qtquickcontrols/examples_quickcontrols_extras_gallery_fonts_LICENSE.txt
cp src/extras/Styles/Flat/fonts/LICENSE.txt %{buildroot}/usr/share/package-licenses/qtquickcontrols/src_extras_Styles_Flat_fonts_LICENSE.txt
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/qml/QtQuick/Controls/ApplicationWindow.qml
/usr/lib64/qt5/qml/QtQuick/Controls/ApplicationWindow.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/BusyIndicator.qml
/usr/lib64/qt5/qml/QtQuick/Controls/BusyIndicator.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Button.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Button.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Calendar.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Calendar.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/CheckBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls/CheckBox.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/ComboBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls/ComboBox.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/GroupBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls/GroupBox.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Label.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Label.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Menu.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Menu.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/MenuBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls/MenuBar.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/AbstractCheckable.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/AbstractCheckable.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/BasicButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/BasicButton.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/BasicTableView.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/BasicTableView.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/CalendarHeaderModel.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/CalendarHeaderModel.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/CalendarUtils.js
/usr/lib64/qt5/qml/QtQuick/Controls/Private/CalendarUtils.jsc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/ColumnMenuContent.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/ColumnMenuContent.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/ContentItem.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/ContentItem.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/Control.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/Control.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/EditMenu.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/EditMenu.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/EditMenu_base.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/EditMenu_base.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/FastGlow.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/FastGlow.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/FocusFrame.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/FocusFrame.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/HoverButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/HoverButton.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/MenuContentItem.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/MenuContentItem.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/MenuContentScroller.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/MenuContentScroller.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/MenuItemSubControls.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/MenuItemSubControls.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/ModalPopupBehavior.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/ModalPopupBehavior.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/ScrollBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/ScrollBar.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/ScrollViewHelper.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/ScrollViewHelper.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/SourceProxy.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/SourceProxy.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/StackView.js
/usr/lib64/qt5/qml/QtQuick/Controls/Private/StackView.jsc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/StackViewSlideDelegate.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/StackViewSlideDelegate.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/Style.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/Style.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/SystemPaletteSingleton.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/SystemPaletteSingleton.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TabBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TabBar.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TableViewItemDelegateLoader.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TableViewItemDelegateLoader.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TableViewSelection.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TableViewSelection.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TextHandle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TextHandle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TextInputWithHandles.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TextInputWithHandles.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TextSingleton.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TextSingleton.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/ToolMenuButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/ToolMenuButton.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TreeViewItemDelegateLoader.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Private/TreeViewItemDelegateLoader.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Private/qmldir
/usr/lib64/qt5/qml/QtQuick/Controls/Private/style.js
/usr/lib64/qt5/qml/QtQuick/Controls/Private/style.jsc
/usr/lib64/qt5/qml/QtQuick/Controls/ProgressBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls/ProgressBar.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/RadioButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls/RadioButton.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/ScrollView.qml
/usr/lib64/qt5/qml/QtQuick/Controls/ScrollView.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Slider.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Slider.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/SpinBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls/SpinBox.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/SplitView.qml
/usr/lib64/qt5/qml/QtQuick/Controls/SplitView.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/StackView.qml
/usr/lib64/qt5/qml/QtQuick/Controls/StackView.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/StackViewDelegate.qml
/usr/lib64/qt5/qml/QtQuick/Controls/StackViewDelegate.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/StackViewTransition.qml
/usr/lib64/qt5/qml/QtQuick/Controls/StackViewTransition.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/StatusBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls/StatusBar.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ApplicationWindowStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ApplicationWindowStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/BasicTableViewStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/BasicTableViewStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/BusyIndicatorStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/BusyIndicatorStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ButtonStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ButtonStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/CalendarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/CalendarStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/CheckBoxStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/CheckBoxStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/CircularButtonStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/CircularButtonStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/CircularGaugeStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/CircularGaugeStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/CircularTickmarkLabelStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/CircularTickmarkLabelStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ComboBoxStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ComboBoxStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/CommonStyleHelper.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/CommonStyleHelper.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/DelayButtonStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/DelayButtonStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/DialStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/DialStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/FocusFrameStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/FocusFrameStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/GaugeStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/GaugeStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/GroupBoxStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/GroupBoxStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/HandleStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/HandleStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/HandleStyleHelper.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/HandleStyleHelper.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/MenuBarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/MenuBarStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/MenuStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/MenuStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/PieMenuStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/PieMenuStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ProgressBarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ProgressBarStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/RadioButtonStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/RadioButtonStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ScrollViewStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ScrollViewStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/SliderStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/SliderStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/SpinBoxStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/SpinBoxStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/StatusBarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/StatusBarStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/StatusIndicatorStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/StatusIndicatorStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/SwitchStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/SwitchStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/TabViewStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/TabViewStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/TableViewStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/TableViewStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/TextAreaStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/TextAreaStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/TextFieldStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/TextFieldStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ToggleButtonStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ToggleButtonStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ToolBarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ToolBarStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ToolButtonStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/ToolButtonStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/TreeViewStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/TreeViewStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/TumblerStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/TumblerStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/arrow-down.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/arrow-down@2x.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/arrow-left.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/arrow-left@2x.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/arrow-right.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/arrow-right@2x.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/arrow-up.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/arrow-up@2x.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/button.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/button_down.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/check.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/check@2x.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/editbox.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/focusframe.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/groupbox.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/header.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/knob.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/leftanglearrow.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/needle.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/progress-indeterminate.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/rightanglearrow.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/scrollbar-handle-horizontal.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/scrollbar-handle-transient.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/scrollbar-handle-vertical.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/slider-groove.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/slider-handle.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/spinner_large.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/spinner_medium.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/spinner_small.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/tab.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Base/images/tab_selected.png
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ApplicationWindowStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ApplicationWindowStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/BusyIndicatorStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/BusyIndicatorStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ButtonStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ButtonStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/CalendarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/CalendarStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/CheckBoxStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/CheckBoxStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ComboBoxStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ComboBoxStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/FocusFrameStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/FocusFrameStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/GroupBoxStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/GroupBoxStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/MenuBarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/MenuBarStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/MenuStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/MenuStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ProgressBarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ProgressBarStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/RadioButtonStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/RadioButtonStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/RowItemSingleton.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/RowItemSingleton.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ScrollViewStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ScrollViewStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/SliderStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/SliderStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/SpinBoxStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/SpinBoxStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/StatusBarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/StatusBarStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/SwitchStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/SwitchStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/TabViewStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/TabViewStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/TableViewStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/TableViewStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/TextAreaStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/TextAreaStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/TextFieldStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/TextFieldStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ToolBarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ToolBarStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ToolButtonStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/ToolButtonStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/TreeViewStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/TreeViewStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Desktop/qmldir
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Flat/libqtquickextrasflatplugin.so
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Flat/qmldir
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/qmldir
/usr/lib64/qt5/qml/QtQuick/Controls/Switch.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Switch.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/Tab.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Tab.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/TabView.qml
/usr/lib64/qt5/qml/QtQuick/Controls/TabView.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/TableView.qml
/usr/lib64/qt5/qml/QtQuick/Controls/TableView.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/TableViewColumn.qml
/usr/lib64/qt5/qml/QtQuick/Controls/TableViewColumn.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/TextArea.qml
/usr/lib64/qt5/qml/QtQuick/Controls/TextArea.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/TextField.qml
/usr/lib64/qt5/qml/QtQuick/Controls/TextField.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/ToolBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls/ToolBar.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/ToolButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls/ToolButton.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/TreeView.qml
/usr/lib64/qt5/qml/QtQuick/Controls/TreeView.qmlc
/usr/lib64/qt5/qml/QtQuick/Controls/libqtquickcontrolsplugin.so
/usr/lib64/qt5/qml/QtQuick/Controls/plugins.qmltypes
/usr/lib64/qt5/qml/QtQuick/Controls/qmldir
/usr/lib64/qt5/qml/QtQuick/Dialogs/DefaultColorDialog.qml
/usr/lib64/qt5/qml/QtQuick/Dialogs/DefaultColorDialog.qmlc
/usr/lib64/qt5/qml/QtQuick/Dialogs/DefaultDialogWrapper.qml
/usr/lib64/qt5/qml/QtQuick/Dialogs/DefaultDialogWrapper.qmlc
/usr/lib64/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qml
/usr/lib64/qt5/qml/QtQuick/Dialogs/DefaultFileDialog.qmlc
/usr/lib64/qt5/qml/QtQuick/Dialogs/DefaultFontDialog.qml
/usr/lib64/qt5/qml/QtQuick/Dialogs/DefaultFontDialog.qmlc
/usr/lib64/qt5/qml/QtQuick/Dialogs/DefaultMessageDialog.qml
/usr/lib64/qt5/qml/QtQuick/Dialogs/DefaultMessageDialog.qmlc
/usr/lib64/qt5/qml/QtQuick/Dialogs/Private/libdialogsprivateplugin.so
/usr/lib64/qt5/qml/QtQuick/Dialogs/Private/plugins.qmltypes
/usr/lib64/qt5/qml/QtQuick/Dialogs/Private/qmldir
/usr/lib64/qt5/qml/QtQuick/Dialogs/WidgetColorDialog.qml
/usr/lib64/qt5/qml/QtQuick/Dialogs/WidgetColorDialog.qmlc
/usr/lib64/qt5/qml/QtQuick/Dialogs/WidgetFileDialog.qml
/usr/lib64/qt5/qml/QtQuick/Dialogs/WidgetFileDialog.qmlc
/usr/lib64/qt5/qml/QtQuick/Dialogs/WidgetFontDialog.qml
/usr/lib64/qt5/qml/QtQuick/Dialogs/WidgetFontDialog.qmlc
/usr/lib64/qt5/qml/QtQuick/Dialogs/WidgetMessageDialog.qml
/usr/lib64/qt5/qml/QtQuick/Dialogs/WidgetMessageDialog.qmlc
/usr/lib64/qt5/qml/QtQuick/Dialogs/images/checkers.png
/usr/lib64/qt5/qml/QtQuick/Dialogs/images/checkmark.png
/usr/lib64/qt5/qml/QtQuick/Dialogs/images/copy.png
/usr/lib64/qt5/qml/QtQuick/Dialogs/images/critical.png
/usr/lib64/qt5/qml/QtQuick/Dialogs/images/crosshairs.png
/usr/lib64/qt5/qml/QtQuick/Dialogs/images/information.png
/usr/lib64/qt5/qml/QtQuick/Dialogs/images/question.png
/usr/lib64/qt5/qml/QtQuick/Dialogs/images/slider_handle.png
/usr/lib64/qt5/qml/QtQuick/Dialogs/images/sunken_frame.png
/usr/lib64/qt5/qml/QtQuick/Dialogs/images/warning.png
/usr/lib64/qt5/qml/QtQuick/Dialogs/images/window_border.png
/usr/lib64/qt5/qml/QtQuick/Dialogs/libdialogplugin.so
/usr/lib64/qt5/qml/QtQuick/Dialogs/plugins.qmltypes
/usr/lib64/qt5/qml/QtQuick/Dialogs/qml/ColorSlider.qml
/usr/lib64/qt5/qml/QtQuick/Dialogs/qml/ColorSlider.qmlc
/usr/lib64/qt5/qml/QtQuick/Dialogs/qml/DefaultWindowDecoration.qml
/usr/lib64/qt5/qml/QtQuick/Dialogs/qml/DefaultWindowDecoration.qmlc
/usr/lib64/qt5/qml/QtQuick/Dialogs/qml/IconButtonStyle.qml
/usr/lib64/qt5/qml/QtQuick/Dialogs/qml/IconButtonStyle.qmlc
/usr/lib64/qt5/qml/QtQuick/Dialogs/qml/IconGlyph.qml
/usr/lib64/qt5/qml/QtQuick/Dialogs/qml/IconGlyph.qmlc
/usr/lib64/qt5/qml/QtQuick/Dialogs/qml/icons.ttf
/usr/lib64/qt5/qml/QtQuick/Dialogs/qml/qmldir
/usr/lib64/qt5/qml/QtQuick/Dialogs/qmldir
/usr/lib64/qt5/qml/QtQuick/Extras/CircularGauge.qml
/usr/lib64/qt5/qml/QtQuick/Extras/CircularGauge.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/DelayButton.qml
/usr/lib64/qt5/qml/QtQuick/Extras/DelayButton.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/Dial.qml
/usr/lib64/qt5/qml/QtQuick/Extras/Dial.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/Gauge.qml
/usr/lib64/qt5/qml/QtQuick/Extras/Gauge.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/PieMenu.qml
/usr/lib64/qt5/qml/QtQuick/Extras/PieMenu.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/Private/CircularButton.qml
/usr/lib64/qt5/qml/QtQuick/Extras/Private/CircularButton.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/Private/CircularButtonStyleHelper.qml
/usr/lib64/qt5/qml/QtQuick/Extras/Private/CircularButtonStyleHelper.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/Private/CircularTickmarkLabel.qml
/usr/lib64/qt5/qml/QtQuick/Extras/Private/CircularTickmarkLabel.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/Private/Handle.qml
/usr/lib64/qt5/qml/QtQuick/Extras/Private/Handle.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/Private/PieMenuIcon.qml
/usr/lib64/qt5/qml/QtQuick/Extras/Private/PieMenuIcon.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/Private/TextSingleton.qml
/usr/lib64/qt5/qml/QtQuick/Extras/Private/TextSingleton.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/Private/qmldir
/usr/lib64/qt5/qml/QtQuick/Extras/StatusIndicator.qml
/usr/lib64/qt5/qml/QtQuick/Extras/StatusIndicator.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/ToggleButton.qml
/usr/lib64/qt5/qml/QtQuick/Extras/ToggleButton.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/Tumbler.qml
/usr/lib64/qt5/qml/QtQuick/Extras/Tumbler.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/TumblerColumn.qml
/usr/lib64/qt5/qml/QtQuick/Extras/TumblerColumn.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/designer/CircularGaugeSpecifics.qml
/usr/lib64/qt5/qml/QtQuick/Extras/designer/CircularGaugeSpecifics.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/designer/DelayButtonSpecifics.qml
/usr/lib64/qt5/qml/QtQuick/Extras/designer/DelayButtonSpecifics.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/designer/DialSpecifics.qml
/usr/lib64/qt5/qml/QtQuick/Extras/designer/DialSpecifics.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/designer/GaugeSpecifics.qml
/usr/lib64/qt5/qml/QtQuick/Extras/designer/GaugeSpecifics.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/designer/PictureSpecifics.qml
/usr/lib64/qt5/qml/QtQuick/Extras/designer/PictureSpecifics.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/designer/PieMenuSpecifics.qml
/usr/lib64/qt5/qml/QtQuick/Extras/designer/PieMenuSpecifics.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/designer/StatusIndicatorSpecifics.qml
/usr/lib64/qt5/qml/QtQuick/Extras/designer/StatusIndicatorSpecifics.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/designer/ToggleButtonSpecifics.qml
/usr/lib64/qt5/qml/QtQuick/Extras/designer/ToggleButtonSpecifics.qmlc
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/circulargauge-icon.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/circulargauge-icon16.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/delaybutton-icon.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/delaybutton-icon16.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/dial-icon.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/dial-icon16.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/gauge-icon.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/gauge-icon16.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/picture-icon.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/picture-icon16.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/piemenu-icon.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/piemenu-icon16.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/statusindicator-icon.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/statusindicator-icon16.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/togglebutton-icon.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/togglebutton-icon16.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/tumbler-icon.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/images/tumbler-icon16.png
/usr/lib64/qt5/qml/QtQuick/Extras/designer/qtquickextras.metainfo
/usr/lib64/qt5/qml/QtQuick/Extras/libqtquickextrasplugin.so
/usr/lib64/qt5/qml/QtQuick/Extras/plugins.qmltypes
/usr/lib64/qt5/qml/QtQuick/Extras/qmldir
/usr/lib64/qt5/qml/QtQuick/PrivateWidgets/libwidgetsplugin.so
/usr/lib64/qt5/qml/QtQuick/PrivateWidgets/plugins.qmltypes
/usr/lib64/qt5/qml/QtQuick/PrivateWidgets/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtquickcontrols/LICENSE.FDL
/usr/share/package-licenses/qtquickcontrols/LICENSE.GPL2
/usr/share/package-licenses/qtquickcontrols/LICENSE.GPL3
/usr/share/package-licenses/qtquickcontrols/LICENSE.GPL3-EXCEPT
/usr/share/package-licenses/qtquickcontrols/LICENSE.LGPL3
/usr/share/package-licenses/qtquickcontrols/examples_quickcontrols_extras_dashboard_fonts_LICENSE
/usr/share/package-licenses/qtquickcontrols/examples_quickcontrols_extras_gallery_fonts_LICENSE.txt
/usr/share/package-licenses/qtquickcontrols/src_extras_Styles_Flat_fonts_LICENSE.txt
